import json
import os,sys,inspect
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet.page import Page

def main(page: Page):
    print('new session!')
    print("Hash:", page.hash)

pglet.app(target=main, web=False)