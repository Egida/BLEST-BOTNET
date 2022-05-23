import os
import time
import subprocess
import colorama
from colorama import Fore, Back, Style
import sys
import random
from sys import platform
if len(sys.argv) < 3:
    exit()

name = sys.argv[1]
mdl = sys.argv[2]
type = 'ddos'
module = "/usr/share/BLEST/core/"+mdl
TARGET_BDADR = ""
PACKETS = ""
THREADS = "100"
INTERFACE = "hci0"


help_modules = '''
BLEST Modül Yardım Menüsü
============================

    Emrler                          Hakkında
    ----------                      ------------
    show options                    Modül seçeneklerini göster
    set <seçenek> <değer>           Belirtilen seçeneği belirtilen değere değiştirin
    back                            Ana çerçeveye geri dön
    run, start                      Başlat, Seçili modülü çalıştır
'''


try:
    flood = input("(\033[4mblest\033[0m)-("+Fore.RED+f"{name}"+Fore.RESET+") > ").strip(" ")
except Exception:
    exit()
flood = flood.split()
while True:
    if flood == []:
        pass
    elif flood[0] == 'help':
        print(help_modules)
    elif flood[0] == 'back' or flood[0] == 'exit' or flood[0] == 'quit':
        sys.exit()
    elif flood[0] == 'show':
        if len(flood) < 2:
            print(Fore.RED + '[-]' + Fore.RESET + ' Show için kullanılabilenler: (options)')
        else:
            try:
                if flood[1] == 'options':
                    options = f'''
> Modül ({Fore.RED}{name}{Fore.RESET}) seçenekleri:

Seçenek             Hakkında                    Değer
---------           ----------                  -------
TARGET_BDADR        Hedef BLE adresi            {TARGET_BDADR}
PACKETS             Paketler Sayı               {PACKETS}
THREADS             Konular sayı (Threads)      {THREADS}
INTERFACE           Kullanılacak BLE arayüzü    {INTERFACE}
'''
                    print(options)
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Bilinmeyen argüment: "'+flood[1]+'"')
            except:
                pass
    elif flood[0] == 'set':
        if len(flood) < 3:
            print(Fore.RED+'[-]'+Fore.RESET+' kullanımı: set <seçenek> <değer>')
        else:
            try:
                if flood[1] == 'TARGET_BDADR' or flood[1] == 'target_bdadr':
                    TARGET_BDADR=flood[2]
                    print(Fore.BLUE+'[i]'+Fore.RESET+' TARGET_BDADR ==> '+TARGET_BDADR)
                elif flood[1] == 'PACKETS' or flood[1] == 'packets':
                    PACKETS=flood[2]
                    print(Fore.BLUE+'[i]'+Fore.RESET+' PACKETS ==> '+PACKETS)
                elif flood[1] == 'THREADS' or flood[1] == 'threads':
                    THREADS=flood[2]
                    print(Fore.BLUE+'[i]'+Fore.RESET+' THREADS ==> '+THREADS)
                elif flood[1] == 'INTERFACE' or flood[1] == 'interface':
                    INTERFACE=flood[2]
                    print(Fore.BLUE+'[i]'+Fore.RESET+' INTERFACE ==> '+INTERFACE)
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz seçenek: "'+flood[1]+'"')
            except:
                pass
    elif flood[0] == 'run' or flood[0] == 'start':
        if TARGET_BDADR == "" or PACKETS == "" or THREADS == "" or INTERFACE == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Lütfen tüm seçenekleri doldurun!')
        else:
            try:
                os.system(f'python3 {module} {TARGET_BDADR} {PACKETS} {THREADS} {INTERFACE}')
            except Exception:
                pass
    else:
        print(Fore.RED + '[-]' + Fore.RESET + ' Emr bulunmadı: "' + flood[0] + '"')
    try:
        flood = input("(\033[4mblest\033[0m)-(" + Fore.RED + f"{name}" + Fore.RESET + ") > ").strip(" ")
    except Exception:
        exit()
    flood = flood.split()