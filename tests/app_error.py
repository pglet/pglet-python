import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import time
import pglet
from pglet import Slider

def main(page):
    def on_change(e):
        print(e.control.value)

    page.add(
        Slider("Test", width='20%', on_change=on_change)
    )
    
    print("before sleep")

    time.sleep(3)

    print("after sleep")

    #raise Exception("Nailed it!")
    a = 3/0

pglet.app("pglet-error", target=main)