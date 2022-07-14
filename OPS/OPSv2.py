try:
    import socket
    import nmap
    import platform
    from os import system
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(1)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system ==  "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")

OpenPorts=[]
ClosedPorts=[]
def IsOpen(host,PortRange):
    sock = socket.socket()
    open = False
    
    for port in range(1,PortRange):
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

print("All Open Ports: "+str(OpenPorts))
print("\n")
print("All Closed Ports: "+str(ClosedPorts))