from os import system
import time

osD=input("Please enter the type of your Operating System [Linux/Windows]: ")
while osD != "Linux" and osD != "Windows" or osD == " " or osD == "":
  print("Invalid Operating System !")
  time.sleep(2)
  osD=input("Please enter the type of your Operating System [Linux/Windows]: ")
if osD == "Linux":
  system("sudo pip3 install auto-py-to-exe")
else:
  system("pip install auto-py-to-exe")
