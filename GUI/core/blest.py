import tkinter
import subprocess
import colorama
from colorama import Fore
import time
import os
import random
colorama.init()
print("Modül içe aktaramıyorum, os.system İşlevi Kullanılıyor...")
try:
    os.system('python3 /usr/share/BLEST/GUI/files/botnet.py --no-import')
except:
    pass