from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import lg, info, setLogLevel
from mininet.util import dumpNodeConnections, moveIntf
from mininet.cli import CLI
from mininet.node import Switch, OVSKernelSwitch
from mininet.nodelib import NAT, LinuxBridge
from mininet.link import TCLink
from mininet.link import Intf
from subprocess import Popen, PIPE, check_output
from time import sleep, time
from datetime import datetime
from multiprocessing import Process
from argparse import ArgumentParser
import sys
import os
from termcolor import cprint
import time
import re
import subprocess
import random

num_hosts_per_router = 5
debug = False
auth = 'localhost'
C = ['1319', '9675', '2475', '3282', '6580']
parser = ArgumentParser('Configure a simple ring network of nodes with static, RIP or single-area OSPF routing in the core.')
parser.add_argument('--sleep', default=3, type=int)
args = parser.parse_args()
if num_hosts_per_router == 1:
    regexp = re.compile('h(\\d+)')
else:
    regexp = re.compile('h(\\d+)-(\\d+)')


def log(s, col='green'):
    if debug:
        cprint(s, col)


class Router(Switch):
    """Defines a new router that is inside a network namespace so that the
    individual routing entries don't collide.
    """
    ID = 0

    def __init__(self, name, **kwargs):
        kwargs['inNamespace'] = True
        Switch.__init__(self, name, **kwargs)
        Router.ID += 1
        self.switch_id = Router.ID

    @staticmethod
    def setup():
        pass

    def start(self, controllers):
        pass

    def stop(self):
        self.deleteIntfs()

    def log(self, s, col='magenta'):
        cprint(s, col)


class Gateway(Switch):
    '''Defines a new gateway that is NOT inside a network namespace.
    '''
    ID = 0

    def __init__(self, name, **kwargs):
        kwargs['inNamespace'] = False
        Switch.__init__(self, name, **kwargs)
        Gateway.ID += 1
        self.switch_id = Gateway.ID

    @staticmethod
    def setup():
        pass

    def start(self, controllers):
        pass

    def stop(self):
        self.deleteIntfs()

    def log(self, s, col='magenta'):
        cprint(s, col)


class LabTopo(Topo):
    def __init__(self, latency_vec, loss_vec):
        super(LabTopo, self).__init__()
        routers = []
        hosts = []
        routers.append(self.addSwitch('s1'))
        routers.append(self.addSwitch('s3'))
        routers.append(self.addSwitch('s5'))
        routers.append(self.addSwitch('s6'))
        routers.append(self.addSwitch('r1'))
        routers.append(self.addSwitch('r2'))
        routers.append(self.addSwitch('r3'))
        routers.append(self.addSwitch('r4'))
        routers.append(self.addSwitch('r5'))
        routers.append(self.addSwitch('r6'))
        idx = 0
        self.addLink('r1', 'r2', bw=1000, delay='%ims' % latency_vec[idx], loss=loss_vec[idx], use_tbf=True)
        idx += 1
        self.addLink('r1', 'r3', bw=1000, delay='%ims' % latency_vec[idx], loss=loss_vec[idx], use_tbf=True)
        idx += 1
        self.addLink('r1', 'r4', bw=1000, delay='%ims' % latency_vec[idx], loss=loss_vec[idx], use_tbf=True)
        idx += 1
        self.addLink('r2', 'r3', bw=1000, delay='%ims' % latency_vec[idx], loss=loss_vec[idx], use_tbf=True)
        idx += 1
        self.addLink('r2', 'r4', bw=100, delay='%ims' % latency_vec[idx], loss=loss_vec[idx], use_tbf=True)
        idx += 1
        self.addLink('r3', 'r4', bw=1000, delay='%ims' % latency_vec[idx], loss=loss_vec[idx], use_tbf=True)
        idx += 1
        self.addLink('r4', 'r6', bw=100, delay='%ims' % latency_vec[idx], loss=loss_vec[idx], use_tbf=True)
        idx += 1
        self.addLink('r2', 'r5', bw=100, delay='%ims' % latency_vec[idx], loss=loss_vec[idx], use_tbf=True)
        idx += 1
        self.addLink('r3', 'r5', bw=100, delay='%ims' % latency_vec[idx], loss=loss_vec[idx], use_tbf=True)
        self.addLink('r1', 's1')
        self.addLink('r3', 's3')
        self.addLink('r5', 's5')
        self.addLink('r6', 's6')
        for i in (1, 3, 5, 6):
            switch = 's%d' % i
            for j in range(1, num_hosts_per_router + 1):
                if num_hosts_per_router == 1:
                    hostname = 'h%d' % i
                else:
                    hostname = 'h%d-%d' % (i, j)
                host = self.addNode(hostname)
                hosts.append(host)
                self.addLink(switch, host)
                if debug:
                    print('Adding host ' + str(hostname) + ' connected to switch ' + str(switch))


def getIP(hostname):
    if num_hosts_per_router == 1:
        netid = regexp.match(hostname).group(1)
        hostid = 1
    else:
        (netid, hostid) = regexp.match(hostname).group(1, 2)
    ip = f'10.0.{netid!s}.{hostid!s}/24'
    return ip


def getGateway(hostname):
    netid = regexp.match(hostname).group(1)
    gw = '10.0.%s.254' % netid
    return gw


def startBindMount(node):
    node.cmd(f'/bin/mkdir -p /var/tmp/run-{node.name!s} && /bin/mount --bind /var/tmp/run-{node.name!s} /run')
    node.waitOutput()


def startRouting(router):
    router.cmd('/bin/mkdir -p /run/quagga && /bin/chown quagga.quagga /run/quagga')
    router.cmd('/bin/mkdir -p /run/frr && /bin/chown frr.frr /run/frr')
    router.waitOutput()
    log('Starting zebra on %s' % router.name)
    router.cmd(f'/usr/lib/frr/zebra -f exam/conf/zebra-{router.name!s}.conf -d -i /tmp/zebra-{router.name!s}.pid > exam/logs/{router.name!s}-zebra-stdout 2>&1')
    router.waitOutput()
    log('Starting staticd on %s if needed' % router.name)
    router.cmd(f'test -f exam/conf/staticd-{router.name!s}.conf && test -x /usr/lib/frr/staticd && /usr/lib/frr/staticd -f exam/conf/staticd-{router.name!s}.conf -d -i /tmp/staticd-{router.name!s}.pid > exam/logs/{router.name!s}-staticd-stdout 2>&1')
    router.waitOutput()
    log('Starting ospfd on %s if needed' % router.name)
    router.cmd(f'test -f exam/conf/ospfd-{router.name!s}.conf && /usr/lib/frr/ospfd -f exam/conf/ospfd-{router.name!s}.conf -d -i /tmp/ospfd-{router.name!s}.pid > exam/logs/{router.name!s}-ospfd-stdout 2>&1', shell=True)
    router.waitOutput()
    log('Starting ripd on %s if needed' % router.name)
    router.cmd(f'test -f exam/conf/ripd-{router.name!s}.conf && /usr/lib/frr/ripd -f exam/conf/ripd-{router.name!s}.conf -d -i /tmp/ripd-{router.name!s}.pid > exam/logs/{router.name!s}-ripd-stdout 2>&1', shell=True)
    router.waitOutput()


def disabletso(node):
    node.cmd("for iface in `/bin/ip link | /bin/grep -- -eth | /usr/bin/cut -f 2 -d ' ' | /usr/bin/cut -f 1  -d '@'` ; do /sbin/ethtool -K $iface tso off ; done")


def setupDNS(node, DNS):
    node.cmd("/bin/mkdir -p /run/resolvconf && /bin/ln -sf /run/resolvconf/resolv.conf /etc/resolv.conf && echo 'nameserver 10.10.10.%i' > /run/resolvconf/resolv.conf && echo 'search commprotocols.net' >> /run/resolvconf/resolv.conf" % (DNS + 1))
    node.waitOutput()


def startSSH(node):
    log('Starting ssh daemon on %s' % node.name)
    node.cmd('/bin/mkdir -p /run/sshd && /usr/sbin/sshd')


def startnginx(node):
    log('Starting nginx web server daemon on %s' % node.name)
    node.cmd('/usr/sbin/nginx')


def startiperf3(node):
    log('Starting iperf3 network performance evaluation server on %s' % node.name)
    node.cmd('/usr/bin/iperf3 -s -f K -D')


def startWebClient(client, server):
    log('Starting simulated web client')
    client.cmd('(while `true` ; do wget http://%s/bigfile.dat -o /dev/null -O - > /dev/null; sleep 30 ; done) &' % server.name)


def main():
    setLogLevel('error')
    nslookup = int(subprocess.check_output('/usr/bin/nslookup google.com | grep server | wc -l', shell=True).strip().decode('utf-8'))
    if debug:
        print('%i lines from nslookup' % nslookup)
    if nslookup == 1:
        print('No Internet connectivity - please ask examiner to check')
        return
    print('This is the 2026 Communication Protocols Lab Exam.')
    print('')
    print('This script MUST be run using sudo (sudo ./examscript)')
    print('')
    while True:
        txt = input('Please VERY CAREFULLY enter your student ID number: ')
        try:
            idnum = int(txt)
            if idnum < 0:
                print('Error: must be a positive integer')
                continue
            break
        except ValueError:
            print('Error: not a valid integer')
    print('Confirming: student ID number %i is valid' % idnum)
    random.seed(idnum)
    os.system('/bin/rm -f /tmp/r*.log /tmp/r*.pid logs/*')
    os.system('/usr/bin/mn -c -v error >/dev/null 2>&1')
    os.system('/bin/killall -9 zebra ospfd ripd named > /dev/null 2>&1')
    latency = random.randint(20, 100)
    lossprob = random.randint(5, 20) / 5
    loss_vec = list((0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    latency_vec = list((3, 3, 3, 3, 3, 3, 3, 3, 3, 3))
    loss_victim = random.randint(0, 5)
    loss_vec[loss_victim] = lossprob
    latency_victim = random.randint(0, 5)
    latency_vec[latency_victim] = latency
    DNS = random.randint(0, 3)
    webclient = random.randint(0, 4)
    webserver = random.randint(5, 19)
    net = Mininet(topo=LabTopo(latency_vec, loss_vec), switch=Router, link=TCLink)
    ifname = subprocess.check_output("ip route | grep default | cut -f 5 -d ' '", shell=True).strip().decode('utf-8')
    ifaddr = subprocess.check_output("ip addr show dev {} | grep 'inet ' | cut -f 6 -d ' ' | cut -f 1 -d '/'".format(ifname), shell=True).strip().decode('utf-8')
    r7 = net.addSwitch('r7', cls=Gateway, inNamespace=False)
    net.addLink('r7', 'r1', bw=1000, delay='10ms', loss=0, use_tbf=True)
    log('Interface name is {}'.format(ifname))
    log('Interface address is {}'.format(ifaddr))
    r7.cmd('/bin/ip addr add 10.1.7.7/24 dev r7-eth1')
    r7.cmd('/bin/ip route add 10.0.0.0/8 via 10.1.7.1')
    net.start()
    for router in net.switches[:-1]:
        log('Starting bind mount on %s' % router.name)
        startBindMount(router)
    for router in net.switches:
        log('Enabling forwarding on %s' % router.name)
        router.cmd('/sbin/sysctl -w net.ipv4.ip_forward=1')
    for router in net.switches[:-1]:
        log('Starting routing, SSH on %s and configuring DNS and TSO' % router.name)
        startRouting(router)
        setupDNS(router, DNS)
        startSSH(router)
        disabletso(router)
    for switch in net.switches[-5:-1]:
        log('Starting bridge on %s' % switch.name)
        switch.cmd('/sbin/brctl addbr br0')
        for idx in range(1, num_hosts_per_router + 2):
            log('Adding interface %s-eth%i' % (switch.name, idx))
            switch.cmd('/sbin/brctl addif br0 %s-eth%i' % (switch.name, idx))
        switch.cmd('/bin/ip link set br0 up')
    net.switches[0].cmd('/bin/ip addr add 10.1.7.1/24 dev r1-eth5')
    log('Starting DNS server on %s' % net.switches[DNS].name)
    net.switches[DNS].cmd('ifconfig -a > /tmp/debug')
    net.switches[DNS].cmd('/bin/mount --bind exam/bind /etc/bind || echo "bind mount failed" >> /tmp/debug')
    net.switches[DNS].cmd('/bin/mkdir /run/named || echo "mkdir failed" >> /tmp/debug')
    net.switches[DNS].cmd('/bin/chown bind.bind /run/named || echo "chown failed" >> /tmp/debug')
    net.switches[DNS].cmd('named -4 -u bind || echo "start of named failed" >> /tmp/debug')
    net.switches[-1].cmd('/usr/sbin/nft flush table nat')
    net.switches[-1].cmd('/usr/sbin/nft add table nat')
    net.switches[-1].cmd("/usr/sbin/nft add chain nat postrouting '{ type nat hook postrouting priority 100; }'")
    net.switches[-1].cmd('/usr/sbin/nft add rule nat postrouting ip saddr 10.0.0.0/8 oif {} snat {}'.format(ifname, ifaddr))
    net.switches[-1].cmd('/bin/ip route add 10.0.2.1/32 via 10.1.7.1')
    net.switches[-1].cmd('/bin/ip route add 10.0.2.254/32 via 10.1.7.1')
    for host in net.hosts:
        log('Starting bind mount, SSH, nginx on %s and setting up DNS & TSO' % host.name)
        startBindMount(host)
        host.cmd('/sbin/ifconfig ' + str(host.name) + '-eth0 ' + str(getIP(host.name)))
        host.cmd('/sbin/route add default gw %s' % getGateway(host.name))
        setupDNS(host, DNS)
        startSSH(host)
        startnginx(host)
        disabletso(host)
    startWebClient(net.hosts[webclient], net.hosts[webserver])
    if debug:
        print('One-way latency on link %i = %ims' % (latency_victim, latency_vec[latency_victim]))
        print('One-way loss probability = %.2f%%' % lossprob)
        print('Web client host is %s' % net.hosts[webclient].name)
        print('Web server host is %s' % net.hosts[webserver].name)
        print('DNS server host is %s' % net.switches[DNS].name)
        print('Faulty link index is %i' % loss_victim)
    CLI(net)
    net.switches[DNS].cmd('/bin/umount /etc/bind')
    net.stop()
    os.system('/usr/bin/killall -9 zebra staticd ospfd ripd named sshd nginx iperf3 > /dev/null 2>&1')


if __name__ == '__main__':
    main()
