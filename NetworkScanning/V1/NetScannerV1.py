"""
Author: @new92
NetScanner: Program for Network Scanning !
"""

#Imports

try:
    import socket
    import http
    import websockets
    import time
    import sys
    import os
    import nmap
    import pyfiglet
    import platform
    from socket import *
    from scapy.all import ARP, Ether, srp
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(2)
    if platform.system == "Windows":
        system("pip3 install -r requirementsV1.txt")
    else:
        system("sudo pip3 install -r requirementsV1.txt")
#End of Imports

#Main Program
netscanner=pyfiglet.figlet_format("NetScanner")
print(netscanner)

time.sleep(1)
print("[+] Network Scanner")
print("\n")
time.sleep(2)
print("[+] Github: @new92")
print("\n")
print("[01] Scan Network for Vulnerabilities")
print("[02] Display Active Devices in the Network")
print("[0] Exit")
option=input("[::] Choose an option: ")
while option != "01" and option != "02" and option != "0" and option != "1" and option != "2":
    print("Invalid option !")
    time.sleep(2)
    option=input("[::] Please enter again: ")
if option == "01" or option == "1":
    time.sleep(1)
    ip=input("Please enter the ip address of the router: ")
    while "." not in ip:
        print("Invalid IP Address !")
        time.sleep(2)
        ip=input("Please enter again the IP of the router: ")

    print("Please wait while the program is scanning the network...")
    for i in range(1, 49000):
        sock = socket(AF_INET, SOCK_STREAM)
        host = gethostbyname(ip)

        connection = sock.connect_ex((host, i))
        if connection == 0:
            print("Port "+str(i)+": OPEN")
        sock.close()
elif option == "02" or option == "2":
    time.sleep(1)
    target_ip=input("Please enter the IP address of the router: ")
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    print("Active devices:")
    time.sleep(2)
    print("IP Address" + " "*18+"MAC Address")
    for client in clients:
        print("\n{:16}    {}".format(client['ip'], client['mac']))
        time.sleep(1)
    print("<END>")
else:
    print("Exiting...")
    time.sleep(2)
    quit(0)
#End of the Program
