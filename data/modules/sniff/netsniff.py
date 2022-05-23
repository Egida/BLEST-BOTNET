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
INTERFACE = "eth0"


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

Seçenek             Hakkında                     Değer
---------           ----------                   -------
INTERFACE           Sniffer için interface       {INTERFACE}
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
                if flood[1] == 'INTERFACE' or flood[1] == 'interface':
                    INTERFACE=flood[2]
                    print(Fore.BLUE+'[i]'+Fore.RESET+' INTERFACE ==> '+INTERFACE)
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz seçenek: "'+flood[1]+'"')
            except:
                pass
    elif flood[0] == 'run' or flood[0] == 'start':
        if INTERFACE == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Lütfen tüm seçenekleri doldurun!')
        else:
            try:
                os.system(f'python3 {module} -i {INTERFACE}')
            except Exception:
                pass
    else:
        print(Fore.RED + '[-]' + Fore.RESET + ' Emr bulunmadı: "' + flood[0] + '"')
    try:
        flood = input("(\033[4mblest\033[0m)-(" + Fore.RED + f"{name}" + Fore.RESET + ") > ").strip(" ")
    except Exception:
        exit()
    flood = flood.split()