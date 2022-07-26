"""
Author: @new92
DHCP Listener: Program for Capturing and Extracting Packets Containing Useful Information 
Not for illegal use !
The Author has no responsibility for the use of this program
"""

#Imports

try:
    import time
    import platform
    from os import system
    from datetime import time
    import sniffer
    import nmap
    import requests
    import scapy
    import http
    import os
    import sys
    import pyfiglet
    from scapy.all import *
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")

#Logo
dhcp = pyfiglet.figlet_format("DHCP   LISTENER")
print(dhcp)

#Main Program
print("\n")
print("[+] Github: @new92")
print("\n")
print("[1] Inititate DHCP Listener")
print("[2] Exit")
option=int(input("[::] Please enter the choice: "))
while option <= 0 or option > 2:
    print("[!] Invalid Option !")
    time.sleep(1)
    option=int(input("[::] Please enter again the option: "))

#Defs

def DHCP_Listener():
    sniff(prn=Disp_Packet, filter="udp and (port 67 or port 68)")

def Disp_Packet(packet):
    mac, ip, hname, vid = [None] * 4
    if packet.haslayer(Ether):
        mac = packet.getlayer(Ether).src
    dhcp_opts = packet[DHCP].options
    for item in dhcp_opts:
        try:
            label, value = item
        except ValueError:
            continue
        if label == "requested_addr":
            ip = value
        elif label == "hostname":
            hname = value.decode()
        elif label == "vendor_class_id":
            vid = value.decode()
    if mac and vid and hname and ip:
        curTime = time.strftime("[%Y-%m-%d - %H:%M:%S]")
        print(f"{curTime} : MAC: {mac} - HOSTNAME: {hname} / {vid} requested {ip}")
if option == 1:
    print("[+] Listener Started...")
    if __name__ == "__main__":
        DHCP_Listener()
else:
    print("[+] Exiting...")
    exit(0)
#End of the Program
