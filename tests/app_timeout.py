import json
import os,sys,inspect
import threading
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Stack, Text, Toolbar, Message

def main():
    i = 1
    evt = threading.Event()
    while True:
        print(i)
        i = i + 1
        #time.sleep(2)
        evt.wait(2)

#th = threading.Thread(target=main, args=(), daemon=True)
#th.start()

def app_main(page):
    print("New session!")

pglet.app(target=main, server="http://localhost:6000")

print("Press ENTER to exit")
input()