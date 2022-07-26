"""
Author: @new92
Spammer: Program for spamming messages on Instagram Accounts
"""

#Imports
try:
    import time
    import platform
    from os import system
    import instapy
    import instabot
    import instagrapi
    import instaloader
    import sniffer
    import nmap
    import os
    import sys
    import art
    from art import tprint
    from getpass import getpass
    from scapy.all import *
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")

#Logo
tprint("SPAMMER",font="tarty1")


#Main Program
print("\n")
print("[+] Program for spamming messages on someone's Instagram :) ")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[1] Start Spamming")
print("[2] Exit")
print("\n")
option=int(input("[::] Please enter an option: "))

while option <= 0 or option > 2 or option == None:
    print("[!] Invalid option !")
    time.sleep(1)
    option=int(input("[::] Please enter again: "))
if option == 1:
    bot1 = instabot.Bot()
    uname=input("[::] Please enter your username: ")
    while uname == None:
        print("[!] Invalid Username !")
        time.sleep(1)
        uname=input("[::] Please enter again your username: ")
    uname = uname.strip()
    passcode = getpass("[::] Please enter your password: ")
    while passcode == None:
        print("[!] Invalid Password !")
        time.sleep(1)
        passcode = getpass("[::] Please enter again your password: ")
    passcode = passcode.strip()
    bot1.login(username=uname,password=passcode)
    receiver = input("[::] Please enter the receiver's username: ")
    while receiver == None:
        print("[!] Invalid Username !")
        time.sleep(1)
        receiver = input("[::] Please enter the receiver's username: ")
    receiver = receiver.strip()
    load = instaloader.Instaloader()
    cid = load.check_profile_id(receiver)
    print(cid)
    time.sleep(1)
    id = input("[::] Please enter the user's id as shown above: ")
    while id == None:
        print("[!] Invalid ID !")
        time.sleep(1)
        id = input("[::] Please enter again the user's id as shown above: ")
    time.sleep(1)
    msg = str(input("[::] Please enter the message to send: "))
    while msg == None:
        print("[!] Invalid Message !")
        time.sleep(1)
        msg = str(input("[::] Please enter again the message to send: "))
    i = 1
    while i > 0:
        try:
            bot1.send_message(msg,id)
        except Exception as e:
            continue
        time.sleep(1)
        print("[!] Message Send !")
else:
    print("[+] Exiting...")
    exit(0)
