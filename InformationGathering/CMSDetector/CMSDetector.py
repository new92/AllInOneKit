"""
Author: @new92
CMSDetector: Program for detecting if a website is using CMS
"""
try:
    import time
    import platform
    from os import system
    import nmap
    import sniffer
    import webbrowser
    import http
    import requests
    import re
    import os
    import sys
    import argparse
    import art
    from art import tprint
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")
#Some Requirements for the Program
def WebSite(website):
    global us_agent
    us_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
    var = requests.get(website, allow_redirects= False, headers= us_agent)
    return var
#Checking if Website is Online
def Is_On(website1):
    print("[+] Website Online Check...")
    time.sleep(1)
    status = False
    try:
        onCheck = WebSite(website1)
    except requests.exceptions.ConnectionError as err:
        print("[!] Website is offline --> "+str(status))
    else:
        if onCheck.status_code == 200 or onCheck.status_code == 301 or onCheck.status_code == 302:
            status = True
            print("[!] Website in online --> "+str(status))
#Checking if Website is Redirecting
def Is_Red(website1):
    print("[+] Redirect Check...")
    time.sleep(1)
    redCheck = requests.get(website1, headers=us_agent)
    if len(redCheck.history) > 0:
        isred = True 
        if '301' in str(redCheck.history[0]) or '302' in str(redCheck.history[0]):
            print("[!] Website Redirect --> "+str(isred))
            time.sleep(1)
            print("[+] Please Verify the Destination In Order to Ensure Accurate Results !")
            time.sleep(1)
            print("[+] The Website is redirecting to: "+str(redCheck))
    elif 'meta http-equiv="REFRESH"' in redCheck.text:
        print("[!] Website Redirect --> "+str(isred))
        time.sleep(1)
        print("[+] Please Verify the Destination In Order to Ensure Accurate Results !")
    else:
        isred = False
        print("[!] Website Redirect --> "+str(isred))
#Wordpress
def WordPress(websitew):
    print("[+] Scanning for Wordpress...")
    time.sleep(1)
    WLGNScan = requests.get(websitew + "/wp-login.php", headers=us_agent)
    if WLGNScan.status_code == 200 and "user_login" in WLGNScan.text and "404" not in WLGNScan.text:
        print("[!] Detected Wordpress Login Page: "+str(websitew + "/wp-login.php"))
    else:
        print("[!] WARNING: Login Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    WADMNScan = requests.get(websitew + "/wp-admin", headers=us_agent)
    if WADMNScan.status_code == 200 and "404" not in WADMNScan.text:
        print("[!] Detected Wordpress Admin Page: "+str(websitew + "/wp-admin"))
    else:
        print("[!] WARNING: Admin Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    WUPGRDScan = requests.get(websitew + "/wp-admin/upgrade.php", headers=us_agent)
    if WADMNScan.status_code == 200 and "404" not in WADMNScan.text:
        print("[!] Detected Wordpress Upgrade Page: "+str(websitew + "/wp-admin/upgrade.php"))
    else:
        print("[!] WARNING: Upgrade Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    WRDMScan = requests.get(websitew + "/readme.html", headers=us_agent)
    if WRDMScan.status_code == 200 and "404" not in WRDMScan.text:
        print("[!] Detected README Page: "+str(websitew + "/readme.html"))
    else:
        print("[!] WARNING: README Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
#Joomla
def Joomla(websitej):
    print("[+] Scanning for Joomla...")
    JADMNScan = requests.get(websitej + "/administrator/")
    if JADMNScan.status_code == 200 and "mod-login-username" in JADMNScan.text and "404" not in JADMScan.text:
        print("[!] Detected Administrator Page: "+str(websitej + "/administrator"))
    else:
        print("[!] WARNING: Administrator Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    JRDMScan = requests.get(websitej + "/readme.txt")
    if JRDMScan.status_code == 200 and "joomla" in JRDMScan.text and "404" not in JRDMScan.text:
        print("[!] Detected README Page: "+str(websitej + "/readme.txt"))
    else:
        print("[!] WARNING: README Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    JTGScan = requests.get(websitej)
    if JTGScan.status_code == 200 and 'name="generator" content=Joomla' in JTGScan.text and "404" not in JTGScan.text:
        print("[!] Detected Joomla Tag on Index !")
    else:
        print("[!] WARNING: Joomla Tag Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    JSTRScan = requests.get(websitej)
    if JSTRScan.status_code == 200 and "joomla" in JSTRScan.text and "404" not in JSTRScan.text:
        print("[!] Detected Joomla Strings on Index !")
    else:
        print("[!] WARNING: Joomla Strings Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    JDIRScan = requests.get(websitej + "/media/com_joomlaupdate/")
    if JDIRScan.status_code == 403 and "404" not in JDIRScan.text:
        print("[!] Detected Directory: "+str(websitej + "/media/com_joomlaupdate/"))
    else:
        print("[!] WARNING: Joomla Directory Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
#Magento
def Magento(websitem):
    print("[+] Scanning for Magento...")
    time.sleep(1)
    MADMNScan = requests.get(websitem + "/index.php/admin/")
    if MADMNScan.status_code == 200 and "login" in MADMNScan.text and "404" not in MADMNScan.text:
        print("[!] Detected Admin Page: "+str(websitem + "/index.php/admin/"))
    else:
        print("[!] WARNING: Admin Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    MRELScan = requests.get(websitem + "/RELEASE_NOTES.txt")
    if MRELScan.status_code == 200 and "magento" in MRELScan.text:
        print("[!] Detected Release Notes Page: "+str(websitem + "/RELEASE_NOTES.txt"))
    else:
        print("[!] WARNING: Release Notes Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    MCScan = requests.get(websitem + "/js/mage/cookies.js")
    if MCScan.status_code == 200 and "404" not in MCScan.text:
        print("[!] Detected Cookies Page: "+str(websitem + "/js/mage/cookies.js"))
    else:
        print("[!] WARNING: Cookies Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    MSTRScan = requests.get(websitem + "/index.php")
    if MSTRScan.status_code == 200 and "/mage/" in MSTRScan.text or "/magento" in MSTRScan.text:
        print("[!] Detected Strings on Index !")
    else:
        print("[!] WARNING: Strings on Index Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    MCSSScan = requests.get(websitem + "/skin/frontend/default/default/css/styles.css")
    if MCSSScan.status_code == 200 and "404" not in MCSSScan.text:
        print("[!] Detected CSS Page: "+str(websitem + "/skin/frontend/default/default/css/styles.css"))
    else:
        print("[!] WARNING: CSS Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    MERRScan = requests.get(websitem + "/errors/design.xml")
    if MERRScan.status_code == 200 and "magento" in MERRScan.text:
        print("[!] Detected Error Page: "+str(websitem + "/errors/design.xml"))
    else:
        print("[!] WARNING: Error Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
#Drupal
def Drupal(websited):
    print("[+] Scanning for Drupal...")
    time.sleep(1)
    DRDMScan = requests.get(websited + "/readme.txt")
    if DRDMScan.status_code == 200 and "drupal" in DRDMScan.text and "404" not in DRDMScan.text:
        print("[!] Detected README Page: "+str(websited + "/readme.txt"))
    else:
        print("[!] WARNING: README Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    DTGScan = requests.get(websited)
    if DTGScan.status_code == 200 and 'name="Generator" content="Drupal"' in DTGScan.text:
        print("[!] Detected Drupal Tag on Index !")
    else:
        print("[!] WARNING: Drupal Tag Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    DCPRTScan = requests.get(websited + "/core/COPYRIGHT.txt")
    if DCPRTScan.status_code == 200 and "Drupal" in DCPRTScan.text and "404" not in DCPRTScan.text:
        print("[!] Detected COPYRIGHT Page: "+str(websited + "/core/COPYRIGHT.txt"))
    else:
        print("[!] WARNING: COPYRIGHT Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    DRDMScan2 = requests.get(websited + "/modules/README.txt")
    if DRDMScan2.status_code == 200 and "drupal" in DRDMScan2.text and "404" not in DRDMScan2.text:
        print("[!] Detected 2nd README Page: "+str(websited + "/modules/README.txt"))
    else:
        print("[!] 2nd README Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    DSTRScan = requests.get(websited)
    if DSTRScan.status_code == 200 and "drupal" in DSTRScan.text:
        print("[!] Detected Strings on Index !")
    else:
        print("[!] WARNING: Strings on Index Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
#PHPMyAdmin
def PHPMYADMIN(websitep):
    print("[+] Scanning for PHPMyAdmin...")
    time.sleep(1)
    PADMNScan = requests.get(websitep)
    if PADMNScan.status_code == 200 and "phpmyadmin" in PADMNScan.text:
        print("[!] Detected Index Page !")
    else:
        print("[!] WARNING: Index Page Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    PPMAScan = requests.get(websitep)
    if PPMAScan.status_code == 200 and "pmahomme" in PPMAScan.text or "pma_" in PPMAScan.text:
        print("[!] Detected Style Links on Index Page !")
    else:
        print("[!] WARNING: Style Links Missing from Index Page !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
    PCONFScan = requests.get(websitep + "/config.inc.php")
    if PCONFScan.status_code == 200 and "404" not in PCONFScan.text:
        print("[!] Detected Configuration File: "+str(websitep + "/config.inc.php"))
    else:
        print("[!] WARNING: Configuration File Missing !")
        time.sleep(1)
        print("[+] Ignoring and Continuing...")
#Main Scanner
def Scanner():
    print("[!] NOTE: Website Examples - https://www.example.com , www.example.com ")
    time.sleep(2)
    website = input("[+] Please enter again the website: ")
    while website == None or not website.endswith(".com") or "www" not in website:
        print("[!] You must enter a website !")
        time.sleep(1)
        website = input("[+] Please enter the website: ")
    if website.startswith("http://"):
        protocol = "http://"
        website = website[7:]
    elif website.startswith("https://"):
        protocol = "https://"
        website = website[8:]
    else:
        protocol = "http://"

    if website.endswith("/"):
        website = website.strip('/')

    website = protocol + website

    time.sleep(1)
    print("[+] Initiating Website Tests...")
    time.sleep(1)
    Is_On(website)
    Is_Red(website)
    time.sleep(1)
    print("[+] Initiating Scan...")
    time.sleep(1)
    WordPress(website)
    Joomla(website)
    Magento(website)
    Drupal(website)
    PHPMYADMIN(website)
    print("[!] Scan Complete !")

#Logo
tprint("CMSDETECTOR",font="tarty1")

#Main Program
print("\n")
print("[+] Program for Detecting the CMS a website is using !")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[1] Initiate Detector")
print("[2] Exit")
option=int(input("[::] Please enter the number: "))
while option <= 0 or option > 2 or option == None:
    print("[!] Invalid Number !")
    time.sleep(1)
    option=int(input("[::] Please enter again the number: "))
if option == 1:
    print("[+] Initiating Scan...")
    time.sleep(1)
    Scanner()
else:
    print("[+] Exiting...")
    exit(0)
