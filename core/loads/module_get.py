import sys
import os
import time
import colorama
from colorama import Fore
colorama.init()
if len(sys.argv) < 2:
    exit()

select = ""
vars = ['.py', '.rb', '.sh']
mod = sys.argv[1]
path = os.listdir("/usr/share/BLEST/core/modules")
dir = None
try:
    if os.path.exists("/usr/share/BLEST/core/modules/"+mod+'.py'):
        dir = False
    else:
        dir = True
except:
    pass

if dir:
    for i in path:
        if os.path.exists("/usr/share/BLEST/core/modules/"+i+"/"+mod+".py"):
            select = "/usr/share/BLEST/core/modules/"+i+"/"+mod+".py"
            break