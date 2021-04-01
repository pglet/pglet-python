import os

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Textbox, Button, Stack

def main(page):
    page.title = "Python Todo with Pglet"
    page.update()
    page.clean(True)
    page.add(Stack(horizontal=True, width='50%', controls=[
        Textbox(placeholder='What needs to be done?', width='100%'), 
        Button("Add")]))
    page.update()
    

#pglet.app("todo-app", target = main)
page = pglet.page("todo-app")
main(page)