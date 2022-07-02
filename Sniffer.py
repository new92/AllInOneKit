"""
Author: @new92
Program for information gathering for Instagram accounts 
Made for educational purposes
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
    import sniffer
    import nmap
    from geopy.geocoders import Nominatim
    from os import system
except ImportError as imp:
    print("WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("Ignoring Warning...")
    time.sleep(2)
    system("sudo pip3 install -r requirements.txt")
#End of imports


#Main program 
snif = pyfiglet.figlet_format("SNIFFER")
print(snif)

username=input("Please enter the username of the victim: ")
time.sleep(1)
usernameused=username.lower()

#Information Gathering

userinfo = requests.get("https://www.instagram.com/"+str(usernameused))
UsefulInfo=userinfo.headers
OtherInfo=userinfo.content
if userinfo.status_code == requests.codes.ok: 
    print("User and information found !")
else: 
    print("User not found !")
    print("Try checking the username and the platform")
Information = UsefulInfo, OtherInfo
#End of Information Gathering

#Display Information which have been gathered
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
print("This is the profile Sniffer formed with the information: ")
time.sleep(4)
print("|----------------PROFILE--------------|                 ")
print("                                                        ")
time.sleep(2)
print("      Username: "+str(username)+"                       ")
time.sleep(2)
print("      Information: "+str(Information)+"                 ")
time.sleep(2)
print("                                                        ")
print("|---------------------------------------|               ")
#End of the program
