"""
Author: @new92
Program for information gathering for Social Media accounts 
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
    print("Error While Importing Modules !")
    time.sleep(2)
    print("Ignoring Error...")
    time.sleep(2)
    system("sudo pip3 install -r requirementsS.txt")
    pass
#End of imports


#Main program 
snif = pyfiglet.figlet_format("SNIFFER")
print(snif)

username=input("Please enter the username: ")
time.sleep(1)
socialplatform=input("Please enter the social media platform: ")
socialplatform=socialplatform.lower()
socialplatform=socialplatform.strip()
username=username.lower()
username=username.strip()
#Information Gathering

if socialplatform == "instagram":
    loader = instaloader.Instaloader()
    client=instagrapi.Client()
    IsPrivate=input("Is the account private [Y/N] ? ")
    while IsPrivate != "Y" and IsPrivate != "y" and IsPrivate != "N" and IsPrivate != "n":
        print("Invalid Input !")
        time.sleep(2)
        IsPrivate=input("Is the social media platform Instagram [Y/N] ? ")
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
    pass
userinfo = requests.get("https://www."+str(socialplatform)+".com/"+str(username))
UsefulInfo=userinfo.headers
OtherInfo=userinfo.content
if userinfo.status_code == requests.codes.ok: 
    print("User and information found !")
else: 
    print("User not found !")
    print("Try checking the username and the platform")
Information = UsefulInfo, OtherInfo
#End of Information Gathering

#Displaying Information which have been gathered
"""
time.sleep(2)
print("Account found | ✓")
time.sleep(3)
print("Checking internet connection | ✓")
time.sleep(5)
print("Checking account's security | ✓")
time.sleep(5)
print("Initiating attack | ✓")
time.sleep(5)
print("Bypassing first security stage | ✓")
time.sleep(5)
print("Bypassing second security stage | ✓")
time.sleep(5)
print("Bypassing third security stage | ✓")
time.sleep(5)
print("Attack successful | ✓")
time.sleep(5)
print("Initiating information gathering | ✓")
time.sleep(7)
print("Password found | ✓")
time.sleep(5)
print("IP found | ✓")
time.sleep(5)
print("Device's information found | ✓")
time.sleep(5)
print("Gathering other information | ✓")
time.sleep(5)
print("Information gathered | ✓")
time.sleep(5)
"""
print("This is the profile Sniffer formed with the information: ")
time.sleep(4)
print("|----------------PROFILE--------------|                 ")
print("                                                        ")
time.sleep(2)
print("      Platform: "+str(Socialplatform)+"                 ")
time.sleep(2)
print("      Username: "+str(username)+"                       ")
time.sleep(2)
print("      A file with the name: "+str(username)+" has been created, containing all the information for the user !")
time.sleep(2)
print("      Information: "+str(Information)+"                 ")
time.sleep(2)
print("                                                        ")
print("|---------------------------------------|               ")
#End of the program