import random
from random import randint
import subprocess
import os
import asyncio
import time

part1 = str(randint(1000, 9999))
part2 = str(randint(1000, 9999))
serialNumberGen = part1 + "-" + part2

def spoof():
    disk = str(input("What is the name of your Hard Disk (exemple : C:) ? : "))
    ask2 = str(input("Last step, are you sure you want to conitnue ? [yes/no]"))
    if ask2 == "yes":
        nom="spoof.bat"      
        fichier=open(nom,'w')
        fichier.write("cd {disk}/Windows/System32/HardDiskSpoofer/not_touch\nvolumeid {disk}\ {serialNumberGen}".format(disk=disk, serialNumberGen=serialNumberGen))
        fichier.close()
        subprocess.run(["spoof.bat"])
        time.sleep(1.0)
        os.remove("spoof.bat")
        print("The spoof is done your new Serial Number is : ", serialNumberGen)
        time.sleep(5.0)
    elif ask2 == "no":
            print("You are a pussy")
            time.sleep(1.0)
    else:
        print("Error, retry to launch the program")
        time.sleep(1.0)
    return spoof
          

print("Hi welcome to Hard Disk Spoofer by Nudryk")
ask1 = str(input("[1] Spoof your Hard Disk\n[2] Exit\nYour choice : "))

if ask1 == "1":
    spoof()
else:
    print("GoodBye !")
    time.sleep(1.0)
                 
          