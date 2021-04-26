import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Icon

def main(page):
    page.title = "Icons example"
    page.gap = 20
    page.update()

    page.add(
        Stack(horizontal=True, controls=[
            Icon("ChangeEntitlements", color='Magenta20'),
            Icon("shop", color='CyanBlue10'),
            Icon("TrainSolid")
        ]),
        Stack(horizontal=True, vertical_align='center', controls=[
            Icon("BlockedSite", color='Orange20', size=25),
            Icon("settings", color='Gray20', size=50),
            Icon("save", color='Blue10', size=100)
        ])        
    )

pglet.app("python-icon", target=main)