import json
import os,sys,inspect
import time
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet

def main(page):
    print('new session!')

pglet.app(target=main, server="localhost:5000")