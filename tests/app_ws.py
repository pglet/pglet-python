import json
import os,sys,inspect
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Stack, Text, Toolbar, Message

def main(page: Page):
    print('new session!')
    print("Hash:", page.hash)
    page.on_hash_change = lambda e: print("New page hash", page.hash)

    txt = Text("Line 1")
    page.add(txt)
    time.sleep(5)

    txt1 = Text("Line 0")
    page.insert(0, txt1)
    time.sleep(5)

    page.controls.append(Text("Line 3"))
    page.controls.pop(1)
    page.update()

pglet.app(target=main, web=False)