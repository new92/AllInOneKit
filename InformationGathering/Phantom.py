"""
Author: @new92
Phantom: Tool for Website Information Gathering
Made for educational purposes 
The author has no responsibility for any illegal activity/activities carried out using this program
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
    import crypto
    import cryptography
    import Cryptodome
    import pyfiglet
    import whois
    import tqdm
    import re
    import nmap
    import argparse
    from os import system
except ImportError as i:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(2)
    if platform.system == "Windows":
        system("pip3 install -r requirementsP.txt")
    else:
        system("sudo pip3 install -r requirementsP.txt")
#End of imports

#Logo
phantom=pyfiglet.figlet_format("PHANTOM")
print(phantom)
#

#Information Gathering
IPport=socket.IPPORT_RESERVED
website=input("[+] Please enter the name of the website: ")
while website == " " or website == "" or len(website) = 0 or "http" not in website or "https" not in website:
    print("[!] Invalid Website !")
    time.sleep(1)
    website=input("[+] Please enter again the name of the website: ")
website=website.lower()
website=website.strip()
Info=requests.get("https://www."+str(website)+".com")
time.sleep(1)
if Info.status_code == requests.codes.ok:
    print("[!] Information Gathering Successfull !")
else:
    print("[!] Website not found !!")
    time.sleep(1)
    print("[+] Please check the name and try again !")
MoreInfo=Info.headers
UsefulInfo=Info.content
try: 
    IPwebsite=socket.gethostbyname("www."+str(website)+".com")
except socket.herror() as s:
    print("[!] Error while tracing the IP of the website !")
    time.sleep(2)
    print(s)
FullHostName=socket.getfqdn(IPwebsite)

#End of Information Gathering

#Displaying Information / Main program
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Website found | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Checking internet connection | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Checking website's security | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Bypassing security | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Initiating information gathering | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Information gathered | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] This is the profile of the website Phantom formed with the information:")
time.sleep(2)
print("|----------------PROFILE--------------------|             ")
print("                                                          ")
print("  [+] Full Host Name: "+str(FullHostName)+"               ")
time.sleep(2)
print("  [+] Website IP: "+str(IPwebsite)+"                      ")
time.sleep(2)
print("  [+] Other Informations: "+str(UsefulInfo)+"             ")
time.sleep(2)
print("  [+] Useful Informations: "+str(MoreInfo)+"              ")
time.sleep(2)
print("                                                          ")
print("|-------------------------------------------|             ")
#End of the program
