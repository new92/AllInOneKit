"""
Author: @new92
Spammer: Program for spamming messages
"""

#Imports
try:
    import instapy
    import instabot
    import instagrapi
    import instaloader
    import sniffer
    import nmap
    import os
    import sys
    import time
    import platform
    import pyfiglet
    from getpass import getpass
    from scapy.all import *
    from os import system
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")

#Logo
spam = pyfiglet.figlet_format("SPAMMER")
print(spam)


#Main Program
print("[+] Github: @new92")
print("\n")
print("[01] Start Spamming")
print("[02] Exit")
print("\n")
option=input("[::] Choose an option: ")

while option != "01" and option != "02" and option != "1" and option != "2":
    print("[!] Invalid option !")
    time.sleep(1)
    option=input("[::] Please enter again: ")
if option == "01" or option == "1":
    bot1 = instabot.Bot()
    uname=input("[+] Please enter your username: ")
    while uname == None:
        print("[!] Invalid Username !")
        time.sleep(1)
        uname=input("[+] Please enter again your username: ")
    uname = uname.strip()
    passcode = getpass("[+] Please enter your password: ")
    while passcode == None:
        print("[!] Invalid Password !")
        time.sleep(1)
        passcode = getpass("[+] Please enter again your password: ")
    passcode = passcode.strip()
    bot1.login(username=uname,password=passcode)
    receiver = input("[+] Please enter the receiver's username: ")
    while receiver == None:
        print("[!] Invalid Username !")
        time.sleep(1)
        receiver = input("[+] Please enter the receiver's username: ")
    receiver = receiver.strip()
    load = instaloader.Instaloader()
    cid = load.check_profile_id(receiver)
    print(cid)
    time.sleep(1)
    id = input("[+] Please enter the user's id as shown above: ")
    while id == None:
        print("[!] Invalid ID !")
        time.sleep(1)
        id = input("[+] Please enter again the user's id as shown above: ")
    time.sleep(1)
    msg = str(input("[+] Please enter the message to send: "))
    while msg == None:
        print("[!] Invalid Message !")
        time.sleep(1)
        msg = str(input("[+] Please enter again the message to send: "))
    i = 1
    while i > 0:
        bot1.send_message(msg,id)
        print("[!] Message Send !")
        continue
else:
    print("[+] Exiting...")
    exit(0)