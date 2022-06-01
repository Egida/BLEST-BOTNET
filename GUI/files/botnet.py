import tkinter
from tkinter import Label, PhotoImage, Tk
import subprocess
import colorama
from colorama import Fore
import time
import os
import sys
import random
file = sys.argv[0]
path = os.path.dirname(file)
if len(sys.argv) < 2:
    pass


def botnet_load():
    def labels():
        welcome = Label(text='Blest Botnet menüsüne hoş geldiniz!', fg='red', bg='black')
    w = Tk()
    w.title("BLEST Framework")
    w.config(bg='black')
    w.geometry('700x550+450+150')
    photo = PhotoImage(file=f"{path}/imgs/botnet.png")
    w.iconphoto(True, photo)
    labels()
    w.mainloop()



try:
    botnet_load()
except Exception as e:
    print('Error: '+str(e))