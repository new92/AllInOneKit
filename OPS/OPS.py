"""
Author: @new92
Program for Scanning the device for open ports
Not for illegal use !
The author has no responsibility for any illegal activities carried out using this program
"""

#Imports
try:
    import nmap
    import sniffer
    import socket
    import time 
    import os 
    import sys
    import requests
    import geocoder
    import crypto 
    import cryptography
    import getpass
    import pyfiglet
    import logging
    import http
    from os import system
except ImportError as imp:
    print("Error while importing modules !")
    time.sleep(2)
    print("Ignoring Error...")
    time.sleep(2)
    system("sudo pip3 install -r requirements.txt")
    pass
#End of Imports

#Logo
OPS=pyfiglet.figlet_format("OPS")
print(OPS)

#Main program

print("[+]Tool for Scanning for open ports")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[01] Scan for Open Ports")
print("[02] Exit")
option=input("Choose an option: ")
while option != "01" and option != "02" and option != "1" and option != "2":
    print("Invalid option !")
    option=input("Please enter again: ")
if option == "01" or option == "1":
    try:
        hostname=socket.gethostname()
        DevIP=socket.gethostbyname(hostname)
    except Exception as e:
        print("Error !")
        print("\n")
        print(e)
    print("Initiating System Scan for Open Ports")
    time.sleep(10)
    try:
        OpenPorts=os.system("nmap --open "+str(DevIP))
        print(OpenPorts)
    except Exception as e: 
        print("Error !")
        print("\n")
        print(e)

else: 
    print("Exiting...")
    time.sleep(2)
    quit(0)
#End of the program
