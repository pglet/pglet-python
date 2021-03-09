import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Button, Textbox

def main(page):
    page.clean()

    def on_click(e):
        name = page.get_value(txtName)
        page.clean()
        page.add(Text(value=f"Hello, {name}!"))

    txtName = Textbox(label="Your name", description="Please enter your full name")
    page.add(
        txtName,
        Button(text='Say hello!', onclick=on_click)
    )

pglet.app(target=main, web=True)