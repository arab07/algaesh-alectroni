import os, platform

print(50*"-")

print("[>>] JOIN MY WHATSAPP GROUP")

print(50*"-")

os.system('xdg-open https://chat.whatsapp.com/GrxWJLqOb7vCwUv765CCfX')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    os.system("python3 run64.py") 


elif bit == '32bit':

    from run32 import infinty

    infinty()
