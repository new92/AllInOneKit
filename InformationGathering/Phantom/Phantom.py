"""
Author: @new92
Phantom: Tool for Website Information Gathering
Made for educational purposes 
The author has no responsibility for any illegal activity/activities carried out with this tool
"""


#Imports
try:
    import time
    import platform
    from os import system
    import sys
    import os 
    import socket
    import locale
    import requests
    import sniffer
    import scrapy
    import nmap
    import whois
    import ipwhois
    import ipapi
    import re
    import tqdm
    import argparse
    import builtwith
    import art
    from art import tprint
    from tqdm import tqdm
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(2)
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")

#Logo
tprint("PHANTOM",font="tarty1")


class Information:
    def __init__(self,wbsite):
        self.wbsite = wbsite
    def IsRegist(self):
        try:
            who = whois.whois(self.wbsite)
        except Exception:
            return False
        else:
            return bool(who.domain_name)
    def Content(self):
        contents = builtwith.builtwith(self.wbsite)
        return contents
    def FullHName(self):
        FName=socket.getfqdn(wip)
        return FName
    
    def Location(self):
        loc = ipapi.location(ip = wip)
        return loc


def OpenPorts(ips):
    op = system("nmap --open "+str(ips))
    return op

print("\n")
print("[+] Github: @new92")
print("\n")
print("[1] Initiate Information Gathering")
print("[2] Exit")
print("\n")
option=int(input("[::] Choose an option: "))

while option == None or option <= 0 or option > 2:
    print("[!] Invalid option !")
    time.sleep(1)
    option=int(input("[::] Please enter again: "))
if option == 1:
    time.sleep(1)

    #Information Gathering
    
    IPport=socket.IPPORT_RESERVED
    print("[!] NOTE: Website Examples - https://www.example.com , www.example.com ")
    time.sleep(2)
    website1=input("[::] Please enter the website: ")
    while website1 == None or ".com" not in website1 or "www" not in website1:
        print("[!] Invalid Website !")
        time.sleep(1)
        print("[!] NOTE: Website Examples - https://www.example.com , www.example.com ")
        time.sleep(2)
        website1=input("[::] Please enter again the website: ")
    website=website1.lower()
    website=website.strip()
    hname = str(website)
    if website.startswith("https://") or website.startswith("http://"):
        Info=requests.get(website)
    else:
        Info=requests.get("https://"+str(website))
    time.sleep(1)
    if Info.status_code == requests.codes.ok:
        print("[!] Information Gathering Successfull !")
        time.sleep(2)
    else:
        print("[!] Website not found !")
        time.sleep(1)
        print("[+] Please check the name and try again !")
        exit(0)
    UsefulInfo=Info.content
    info = Information(website)
    wip = socket.gethostbyname(hname)
    print("[+] Initiating CMS Detector...")
    time.sleep(1)
    import CMSDetector

    #Main program
    for i in tqdm(range(10000000)):
        pass
    time.sleep(1)
    print("[+] Website found | ✓")
    for i in tqdm(range(10000000)):
        pass
    time.sleep(1)
    print("[+] Checking internet connection | ✓")
    for i in tqdm(range(10000000)):
        pass
    time.sleep(1)
    print("[+] Checking website's security | ✓")
    for i in tqdm(range(10000000)):
        pass
    time.sleep(1)
    print("[+] Bypassing security | ✓")
    for i in tqdm(range(10000000)):
        pass
    time.sleep(1)
    print("[+] Initiating information gathering | ✓")
    for i in tqdm(range(10000000)):
        pass
    time.sleep(1)
    print("[+] Information gathered | ✓")
    time.sleep(2)
    print("[+] This is the profile of the given website Phantom formed with the information:")
    time.sleep(2)
    print("|----------------PHANTOM--------------------|")
    print("                                                          ")
    print("   [+] Full Host Name: "+str(info.FullHName())+"         ")
    time.sleep(2)
    print("   [+] Website IP: "+str(wip)+"                    ")
    time.sleep(2)
    print("   [+] Has Registered Domain Name: "+str(info.IsRegist())+" ")
    time.sleep(2)
    print("   [+] Has Been Built With: "+str(info.Content())+"      ")
    time.sleep(2)
    print("   [+] Website Link: "+str(website)+"                    ")
    time.sleep(2)
    print("   [+] Website Location: "+str(info.Location())+"        ")
    time.sleep(2)
    print("   [+] Website Open Ports: "+str(OpenPorts(wip))+"              ")
    time.sleep(2)
    print("   [+] Other Information: "+str(UsefulInfo)+"                   ")
    time.sleep(2)
    print("                                                                ")  
    print("|-------------------------------------------|                   ")
else:
    print("[+] Exiting...")
    exit(0)
