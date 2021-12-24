import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import IFrame

def main(page):
    page.title = "IFrame example"
    page.gap = 20
    page.add(
        IFrame(src='https://pglet.io', title='sample image', width="50%", height="300", border="1")
    )

pglet.app("python-iframe", target=main)