import socket
from socket import AF_INET, SOCK_STREAM
import colorama
from colorama import Fore
colorama.init()
# sadece bir test fayl

try:
    s = socket.socket(AF_INET, SOCK_STREAM)
    s.connect("127.0.0.1")
except:
    pass