(이미지 Network Topology lab 2)

h1, h2, h3 ... h8 은 호스트(Host) 를 의미해. 노트북 아이콘으로 표시되어 있지? 실제 네트워크에서 컴퓨터, 즉 데이터를 보내거나 받는 최종 사용자 장치(end device) 에 해당해. 각 호스트는 하나의 인터페이스(eth0)와 하나의 IP 주소를 가지고 있어. 예를 들어 h1은 10.0.1.1, h2는 10.0.2.1 이런 식이야.
r1, r2, r3 ... r9 는 라우터(Router) 를 의미해. 라우터 아이콘(원통형 장치)으로 표시되어 있고, 여러 개의 인터페이스(eth1, eth2, eth3...)를 가지고 있어. 라우터는 서로 다른 네트워크 사이에서 패킷을 전달(forwarding) 하는 역할을 해. 예를 들어 h1에서 h5로 데이터를 보내려면 중간에 여러 라우터를 거쳐야 하는데, 라우터들이 경로를 결정해서 패킷을 다음 목적지로 넘겨주는 거야.
참고로 r9 (NAT) 는 특별한 라우터인데, 이 내부 네트워크를 외부 인터넷에 연결해주는 역할을 해. NAT(Network Address Translation)를 통해 내부 사설 IP 주소(10.x.x.x)를 외부 주소로 변환해줘.
쉽게 비유하면, 호스트(h)는 집, 라우터(r)는 교차로라고 생각하면 돼. 편지(패킷)가 집에서 출발해서 여러 교차로를 거쳐 목적지 집에 도착하는 구조야.


### mininet 접속
comm-protocol-labs 에서 'sudo start.py' 실행

### xterm 명령어 
- xterm h3
mininet에서 h3라는 호스트에 접속

### ping 명령어 예시 
- ping -c 5 10.10.10.3
10.10.10.3(h3) 이라는 호스트로 5개의 'icmp(ex 'icmp_seq=1')' 라는 핑 체크를 목적으로 하는 패킷을 보냄. 2개 보내면 'ping -c 2 10.10.10.3'

### ip addr
- ip addr
In this case, the MAC address of the first physical interface h6-eth0 is 52:c4:44:86:73:c6,
and the IP address/netmask of the interface is 10.0.6.1/24
- ex) 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
inet 127.0.0.1/8 scope host lo
valid_lft forever preferred_lft forever
inet6 ::1/128 scope host
valid_lft forever preferred_lft forever
2: h6-eth0@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb state UP group default qlen 1000
link/ether 52:c4:44:86:73:c6 brd ff:ff:ff:ff:ff:ff link-netnsid 0
inet 10.0.6.1/24 brd 10.0.6.255 scope global h6-eth0
valid_lft forever preferred_lft forever
inet6 fe80::50c4:44ff:fe86:73c6/64 scope link
valid_lft forever preferred_lft forever

위 예시에서 127.0.0.1는 로컬호스트, 본인을 의미하고 10.0.6.1 같은건 연결된 호스트 혹은 라우터를 의미함

#### MAC 주소 = 주민등록번호 — 태어날 때(제조될 때) 부여되고, 기본적으로 바뀌지 않는 고유한 식별자
#### IP 주소 = 집 주소 — 이사하면(네트워크가 바뀌면) 바뀔 수 있는 논리적 주소


