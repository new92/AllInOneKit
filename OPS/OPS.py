"""
Author: @new92
Program for Scanning Open Ports of a device
The author has no responsibility for the use of this program
"""

#Imports
try:
    import time
    import platform
    from os import system
    import nmap
    import sniffer
    import socket 
    import os
    import sys
    import requests
    import getpass
    import pyfiglet
    import logging
    import http
    import art
    from art import tprint
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
tprint("OPS",font="tarty1")

#Main program

print("\n")
print("[+]Tool for Scanning for open ports")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[1] Scan for Open Ports")
print("[2] Exit")
option=int(input("[::] Choose an option: "))
while option <= 0 or option > 2 or option == None:
    print("[!] Invalid option !")
    option=int(input("[::] Please enter again: "))
if option == 1:
    try:
        hostname=socket.gethostname()
        DevIP=socket.gethostbyname(hostname)
    except Exception as e:
        print("[!] Error !")
        time.sleep(1)
        print("\n")
        print(e)
    print("[+] Initiating System Scan for Open Ports")
    time.sleep(10)
    try:
        system("nmap --open "+str(DevIP))
    except Exception as e: 
        print("[!] Error !")
        time.sleep(1)
        print("\n")
        print(e)

else: 
    print("[+] Exiting...")
    exit(0)
