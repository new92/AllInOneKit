"""
Author: @new92
NetScanner: Program for Network Scanning !
"""

#Imports

try:
    import time
    import platform
    from os import system
    import socket
    import http
    import websockets
    import sys
    import os
    import nmap
    import sniffer
    import tqdm
    import art
    from art import tprint
    from socket import *
    from tqdm import tqdm
    from scapy.all import ARP, Ether, srp
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")


#Main Program
tprint("NETSCANNER",font="tarty1")

print("\n")
print("[+] Program for Network Scanning")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[01] Scan Network for Vulnerabilities")
print("[02] Display Active Devices in the Network")
print("[0] Exit")
option=int(input("[::] Choose an option: "))
while option < 0 or option > 2 or option == None:
    print("[!] Invalid option !")
    time.sleep(1)
    option=input("[::] Please enter again: ")
if option == 1:
    time.sleep(1)
    ip=input("[::] Please enter the ip address of the router: ")
    while "." not in ip or ip == None:
        print("[!] Invalid IP Address !")
        time.sleep(2)
        ip=input("[::] Please enter again the IP of the router: ")

    lport = input("[::] Please enter the last port to scan: ")
    while lport == None:
        print("[!] Invalid Parameter !")
        time.sleep(1)
        lport = input("[::] Please enter the last port to scan: ")
    print("[+] Please wait while the program is scanning the network...")
    for b in tqdm(range(1000000)):
        pass
    for i in range(1, 49000):
        sock = socket(AF_INET, SOCK_STREAM)
        host = gethostbyname(ip)

        connection = sock.connect_ex((host, i))
        if connection == True:
            print("Port "+str(i)+": OPEN")
        sock.close()
elif option == "02" or option == "2":
    time.sleep(1)
    rout_ip=input("[::] Please enter the IP address of the router: ")
    arp = ARP(pdst=rout_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    res = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    for sent, received in res:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    print("[+] Active devices:")
    time.sleep(2)
    print("IP Address" + " "*18+"MAC Address")
    for client in clients:
        print("\n{:16}    {}".format(client['ip'], client['mac']))
        time.sleep(1)
    print("<END>")
else:
    print("[+] Exiting...")
    exit(0)
