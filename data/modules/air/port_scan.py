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
type = 'air'
module = "/usr/share/BLEST/core/"+mdl
TARGET = ""
START_PORT = ""
END_PORT = ""



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

Seçenek             Hakkında                Değer
---------           ----------              -------
TARGET              Hedef Adres             {TARGET}
START_PORT          Hedef Başlangıç Port    {START_PORT}
END_PORT            Başlangıçın sonu Port   {END_PORT}
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
                if flood[1] == 'TARGET' or flood[1] == 'target':
                    TARGET=flood[2]
                    print(Fore.BLUE+'[i]'+Fore.RESET+' TARGET ==> '+TARGET)
                elif flood[1] == 'START_PORT' or flood[1] == 'start_port':
                    START_PORT=flood[2]
                    print(Fore.BLUE+'[i]'+Fore.RESET+' START_PORT ==> '+START_PORT)
                elif flood[1] == "END_PORT" or flood[1] == 'end_port':
                    END_PORT=flood[2]
                    print(Fore.BLUE+'[i]'+Fore.RESET+' END_PORT ==> '+END_PORT)
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz seçenek: "'+flood[1]+'"')
            except:
                pass
    elif flood[0] == 'run' or flood[0] == 'start':
        if TARGET == "" or  START_PORT == "" or END_PORT == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Lütfen tüm seçenekleri doldurun!')
        else:
            try:
                os.system(f'python3 {module} {TARGET} {START_PORT} {END_PORT}')
            except Exception:
                pass
    else:
        print(Fore.RED + '[-]' + Fore.RESET + ' Emr bulunmadı: "' + flood[0] + '"')
    try:
        flood = input("(\033[4mblest\033[0m)-(" + Fore.RED + f"{name}" + Fore.RESET + ") > ").strip(" ")
    except Exception:
        exit()
    flood = flood.split()