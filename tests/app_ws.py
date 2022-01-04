import os
import sys
import inspect
import time
import logging

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from pglet import Page, Stack, Text, Toolbar, Message
import pglet

os.environ["PGLET_LOG_LEVEL"] = "debug"
logging.basicConfig(level=logging.DEBUG)

def main(page: Page):
    print('new session!')
    print("Hash:", page.hash)
    print("Width:", page.width, "Height:", page.height)
    page.on_hash_change = lambda e: print("New page hash", page.hash)
    page.on_resize = lambda e: print("New page size:", page.width, page.height)

    txt = Text("Line 1")
    page.add(txt)
    time.sleep(5)

    txt1 = Text("Line 0")
    page.insert(0, txt1)
    time.sleep(5)

    page.controls.append(Text("Line 3"))
    page.controls.pop(1)
    page.update()


pglet.app("page1", target=main, web=False)
