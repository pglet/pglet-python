import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Button, Stack, Textbox

def main(page):
    page.title = "Counter"
    page.update()

    def on_click(e):
        try:
            count = int(txt_number.value)

            txt_number.error_message = ""

            if e.data == '+':
                txt_number.value = count + 1

            elif e.data =='-':
                txt_number.value = count - 1

        except ValueError:
            txt_number.error_message = "Please enter a number"

        page.update()

    txt_number = Textbox(value='0', align='right')

    page.add(
        Stack(horizontal = True, controls=[
            Button('-', on_click=on_click, data='-'),
            txt_number,
            Button('+', on_click=on_click, data='+'),
        ])
    )

pglet.app("counter", target=main)