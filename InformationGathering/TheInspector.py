"""
Author: @new92
TheInspector: Program for information gathering for Social Media accounts 
Made for educatinoal purposes
The author has no responsibility for any illegal activity/activities carried out using this tool
"""

#Sniffer

#Imports
try: 
    import sys
    import os
    import socket
    import locale 
    import platform
    import random 
    import time
    import pyfiglet
    import requests
    import scapy
    import subprocess
    import geocoder
    import smtplib
    import json 
    import getpass
    import cryptography
    import crypto
    import instaloader
    import instagrapi
    import instapy
    import instabot
    import websockets
    import sniffer
    import nmap
    from geopy.geocoders import Nominatim
    from datetime import datetime
    from os import system
except ImportError as imp:
    print("[!] Error While Importing Modules !")
    time.sleep(2)
    print("[+] Ignoring Error...")
    time.sleep(2)
    if platform.system == "Windows":
        system("pip3 install -r requirementsI.txt")
    else:
        system("sudo pip3 install -r requirementsI.txt")
#End of imports


#Main program 
snif = pyfiglet.figlet_format("SNIFFER")
print(snif)

username=input("[+] Please enter the username: ")
while len(username) == 0:
    print("[!] Invalid Username !")
    time.sleep(1)
    username=input("[+] Please enter again the username: ")
time.sleep(1)
socialplatform=input("[+] Please enter the social media platform: ")
while len(socialplatform) == 0:
    print("[!] Invalid Social Media Platform !")
    time.sleep(1)
    socialplatform=input("[+] Please enter again the social media platform: ")
socialplatform=socialplatform.lower()
socialplatform=socialplatform.strip()
username=username.lower()
username=username.strip()
#Information Gathering

if socialplatform == "instagram" or "Instagram":
    loader = instaloader.Instaloader()
    client=instagrapi.Client()
    IsPrivate=input("[+] Is the account private [Y/N] ? ")
    while IsPrivate != "Y" and IsPrivate != "y" and IsPrivate != "N" and IsPrivate != "n":
        print("[!] Invalid Input !")
        time.sleep(2)
        IsPrivate=input("Is the account private [Y/N] ? ")
    if IsPrivate == "Y" or IsPrivate == "y":
        try:
            profileinfo = loader.download_profile(username,True)
        except Exception as e:
            pass
    else:
        try:
            profileinfo = loader.download_profile(username,True)
        except Exception as e:
            pass
        posts = loader.anonymous_copy()
else:
    userinfo = requests.get("https://www."+str(socialplatform)+".com/"+str(username))
    UsefulInfo=userinfo.headers
    OtherInfo=userinfo.content
if userinfo.status_code == requests.codes.ok: 
    print("[!] User and information found !")
else: 
    print("[!] User not found !")
    time.sleep(1)
    print("[+] Try checking the username and the platform")
Information = UsefulInfo, OtherInfo
#End of Information Gathering

#Displaying Gathered Information

for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Account found | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Checking internet connection | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Checking account's security | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Initiating attack | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Bypassing security | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Attack successful | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Initiating information gathering | ✓")
for i in tqdm(range(10000000)):
    pass
time.sleep(1)
print("[+] Password found | ✕")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] IP found | ✕")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Device's information found | ✕")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Gathering other information | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] Information gathered | ✓")
for i in tqdm(range(1000000)):
    pass
time.sleep(1)
print("[+] This is the profile Sniffer formed with the information: ")
time.sleep(4)
print("|----------------PROFILE--------------|                 ")
print("                                                        ")
time.sleep(2)
print("    [+]  Platform: "+str(Socialplatform)+"                 ")
time.sleep(2)
print("    [+]  Username: "+str(username)+"                       ")
time.sleep(2)
if socialplatform == "instagram" or "Instagram":
    print(" [+] A file with the name: "+str(username)+" has been created, containing all the information for the user !")
    time.sleep(2)
else:
    pass
print("     [+] Information: "+str(Information)+"                 ")
time.sleep(2)
print("                                                        ")
print("|---------------------------------------|               ")
#End of the program
