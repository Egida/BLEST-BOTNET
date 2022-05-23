import socket
import sys
import colorama
from colorama import Fore


def scanHost(ip, startPort, endPort):
    print(Fore.BLUE+'[i]'+Fore.RESET+' Ana Bilgisayarda TCP bağlantı noktası taraması başlatiliyor %s' % ip)
    tcp_scan(ip, startPort, endPort)

def scanRange(network, startPort, endPort):
    print(Fore.BLUE+'[i]'+Fore.RESET+' Ağda TCP bağlantı noktası taraması başlatı %s.0' % network)
    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, startPort, endPort)
    print(Fore.YELLOW+'[+]'+Fore.RESET+'Ağda TCP taraması %s.0 Tamamlandı' % network)


def tcp_scan(ip, startPort, endPort):
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip, port)):
                print(Fore.YELLOW+'[+]'+Fore.RESET+' %s:%d/TCP açık' % (ip, port))
                tcp.close()
                
        except Exception:
            pass


if __name__ == '__main__':
    socket.setdefaulttimeout(0.01)
    if len(sys.argv) < 4:
        print('Usage: ./nmap.py <IP address> <start port> <end port>')
        print('Example: ./nmap.py 192.168.1.10 1 65535\n')
        print('Usage: ./nmap.py <network> <start port> <end port> -n')
        print('Example: ./nmap.py 192.168.1 1 65535 -n')

    elif len(sys.argv) >= 4:
        network   = sys.argv[1]
        startPort = int(sys.argv[2])
        endPort   = int(sys.argv[3])

    if len(sys.argv) == 4:
        scanHost(network, startPort, endPort)

    if len(sys.argv) == 5:
        scanRange(network, startPort, endPort)
