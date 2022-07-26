"""
Author: @new92
OPSv2: Program similar to OPS but upgraded and faster !
"""

#Imports
try:
    import time
    import platform
    from os import system
    import socket
    import nmap
    import sniffer
    import art
    from art import tprint
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(1)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system ==  "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")

#Logo
tprint("OPSV2",font="tarty1")

#User Input 
print("\n")
print("[+] Github: @new92")
print("\n")
print("[01] Scan For Open Ports")
print("[02] Exit")
option=input("[+] Please enter the option: ")
while option != "01" and option != "02" and option != "1" and option != "2":
    print("[!] Invalid Option !")
    time.sleep(1)
    print("[+] Please enter again the option: ")
if option == "01" or option == "1":

    #Def
    OpenPorts=[]
    ClosedPorts=[]
    def IsOpen(host,PortRange):
        sock = socket.socket()
        open = False
    
        for port in range(1,PortRange+1):
            try:
                connection = sock.connect((host,port))
                sock.settimeout(0.2)
                if connection == True:
                    OpenPorts.append(port)
                    print("[+] Port: "+str(port)+" is open")
            except:
                ClosedPorts.append(port)
                print("[+] Port: "+str(port)+" is closed")
        sock.close()

#Main Program

    host = input("[+] Please enter the host: ")

    PortRange = int(input("[+] Please enter the last port to scan: "))

    print("[+] Please wait while the program is scanning your device...")

    IsOpen(host, PortRange)

    print("[+] All Open Ports: "+str(OpenPorts))
    print("[+] All Closed Ports: "+str(ClosedPorts))
else:
    print("[+] Exiting...")
    exit(0)
