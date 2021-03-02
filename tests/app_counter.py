import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Button, Stack, Textbox

def main(page):
    page.update(Page(title="Counter"))
    page.clean()

    def on_click(e):
        try:
            count = int(page.get_value('number'))
            #if we get here the number is int
            page.send('set number errorMessage=""')

            if e.data == '+':
                page.set_value('number', count + 1)

            elif e.data =='-':
                page.set_value('number', count - 1)

        except ValueError:
            page.send('set number errorMessage="Please enter a number"')  

    page.add(
        Stack(horizontal = True, controls=[
            Button(text='-', onclick=on_click, data='-'),
            Textbox(id='number', value = '0', align = 'right'),
            Button(text='+', onclick=on_click, data='+'),
        ])
    )

pglet.app("inesa-counter-app", target = main, web = True)