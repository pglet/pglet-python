import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Slider

def main(page):
    def on_change(e):
        print(e.control.value)

    page.add(
        Slider("Test", width='20%', on_change=on_change)
    )

pglet.app("pglet-slider", target=main)