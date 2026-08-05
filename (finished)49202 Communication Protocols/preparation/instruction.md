Laboratory Exam Instructions
The exam will run in week 12 on the 13th and 15th of May 2026. Please make sure to attend at your allocated lab time and day. The exam should take no more than 1 hour to complete, but I will give you 110 minutes to complete and submit your results. The lab test is worth 25% of your marks.

The procedure is as follows:

Start your virtual machine
You will be handed the instructions & questions by your exam supervisor
At the start of your exam, perform the following commands:
cd ~/comm-protocols-labs
git pull (NOTE - if this doesn't work, try git stash first)
cd exam
sudo ./examscript
You will be prompted to enter your student ID number. Please enter it very carefully and double-check before proceeding. If you enter it incorrectly, press ctrl C to abort and then run it again.

This starts a mininet environment with the network configuration described in the instructions. However, the parameters of the network will be DIFFERENT for every student. You will be asked a series of questions about your network, which you will need to solve using standard Linux networking commands (such as route, ifconfig, ip, traceroute, ping, iperf3, and of course Wireshark). You do NOT need to do any socket programming in this lab exam.

