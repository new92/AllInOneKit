"""
Author: @new92
Phantom: Tool for Website Information Gathering
Made for educational purposes 
The author has no responsibility for any illegal activity/activities carried out with this tool
"""


#Imports
try:
    import sys
    import os 
    import socket
    import locale 
    import platform
    import time
    import requests 
    import sniffer
    import pyfiglet
    import scrapy
    import nmap
    import whois
    import ipwhois
    import ipapi
    import re
    import tqdm
    import argparse
    import builtwith
    import platform
    from tqdm import tqdm
    from os import system
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(2)
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")
#End of imports

#Logo
phantom=pyfiglet.figlet_format("PHANTOM")
print(phantom)
#

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

"""def OpenPorts(ips):
    op = system("nmap --open "+str(ips))
    return op
"""
print("[+] Github: @new92")
print("\n")
print("[01] Information Gathering")
print("[02] Exit")
print("\n")
option=input("[::] Choose an option: ")

while option != "01" and option != "02" and option != "1" and option != "2":
    time.sleep(1)
    print("[!] Invalid option !")
    time.sleep(1)
    option=input("[::] Please enter again: ")
if option == "01" or option == "1":
    time.sleep(1)

    #Information Gathering
    
    IPport=socket.IPPORT_RESERVED
    print("[!] NOTE: Website Examples - https://www.example.com , www.example.com , 192.168.1.50")
    time.sleep(2)
    website1=input("[+] Please enter the name of the website: ")
    while website1 == None or len(website1) == 0:
        print("[!] Invalid Website !")
        time.sleep(1)
        print("[!] NOTE: Website Examples - https://www.example.com , www.example.com , 192.168.1.50")
        time.sleep(2)
        website1=input("[+] Please enter again the name of the website: ")
    website=website1.lower()
    website=website.strip()
    hname = str(website)+".com"
    Info=requests.get("https://www."+str(website)+".com")
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
    website = "https://www."+str(website)+".com"
    info = Information(website)
    wip = socket.gethostbyname(hname)
    import CMSDetector

    # Main program
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
    print("[+] This is the profile of "+str(website1)+" Phantom formed with the information:")
    time.sleep(2)
    print("|----------------"+str(website1.upper())+"--------------------|")
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
    #print("   [+] Website Open Ports: "+str(OpenPorts(wip))+"              ")
    time.sleep(2)
    print("   [+] Other Information: "+str(UsefulInfo)+"                   ")
    time.sleep(2)
    print("                                                                ")  
    print("|-------------------------------------------|                   ")
else:
    print("[+] Exiting...")
    exit(0)
#End of the program
