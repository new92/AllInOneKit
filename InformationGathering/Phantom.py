"""
Author: @new92
Anubis: Tool for Website Information Gathering
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
    import crypto
    import cryptography
    import Cryptodome
    import pyfiglet
    import whois
    import re
    import argparse
    from os import system
except ImportError as i:
    print("WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("Ignoring Warning...")
    time.sleep(2)
    system("sudo pip3 install -r requirements.txt")
#End of imports

#Logo
phantom=pyfiglet.figlet_format("PHANTOM")
print(phantom)
#

#Information Gathering
IPport=socket.IPPORT_RESERVED
website=input("Please enter the name of the website: ")
while website == " " or website == "" or len(website) <= 0 or "http" not in website or "https" not in website:
    print("Invalid Website !")
    time.sleep(1)
    website=input("Please enter again the name of the website: ")
website=website.lower()
website=website.strip()
Info=requests.get("https://www."+str(website)+".com")
time.sleep(1)
if Info.status_code == requests.codes.ok:
    print("Information Gathering Successfull !")
else:
    print("Website not found !!")
    print("Please check the name and try again !")
MoreInfo=Info.headers
UsefulInfo=Info.content
try: 
    IPwebsite=socket.gethostbyname("www."+str(website)+".com")
except socket.herror() as s:
    print("Error while tracing the IP of the website !")
    print(s)
FullHostName=socket.getfqdn(IPwebsite)

#End of Information Gathering

#Displaying Information / Main program
print("Website found | ✓")
time.sleep(3)
print("Checking internet connection | ✓")
time.sleep(5)
print("Checking website's security | ✓")
time.sleep(5)
print("Bypassing security | ✓")
time.sleep(5)
print("Initiating information gathering | ✓")
time.sleep(7)
print("Information gathered | ✓")
time.sleep(5)
print("This is the profile of the website Phantom formed with the information:")
time.sleep(2)
print("|----------------PROFILE--------------------|")
print("                                                          ")
print("      Full Host Name: "+str(FullHostName)+"               ")
time.sleep(2)
print("      Website IP: "+str(IPwebsite)+"                      ")
time.sleep(2)
print("      Other Informations: "+str(UsefulInfo)+"             ")
time.sleep(2)
print("      Useful Informations: "+str(MoreInfo)+"              ")
time.sleep(2)
print("                                                          ")
print("|-------------------------------------------|             ")
#End of the program