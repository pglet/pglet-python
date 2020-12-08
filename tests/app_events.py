import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import time
import pglet
from pglet import Text, Textbox, Button, Progress

page = pglet.page("index", no_window=True)
page.clean()

def say_hello_click(e):
    name = page.get_value(txt)
    if name == "":
        txt.error_message = "Name cannot be blank"
        btn.text = "Say it again!"
        page.update(txt, btn)
    else:
        page.remove(txt, btn)
        page.add(Text(value=f'Hello, {name}!'), at=0)

txt = Textbox(label="Your name")
btn = Button(text="Say hello", primary=True)
btn.onclick = say_hello_click
cancel = Button(text="Cancel", onclick=lambda e: print("Cancel clicked"))

page.add(txt, btn, cancel)
print("added #1")

time.sleep(5)

page.clean()
page.add(txt, btn, cancel)
print("added #2")

time.sleep(5)

cancel.text = "Back to main menu"
page.update(cancel)

progr = page.add(Progress(label="Doing something...", width="30%"))
for i in range(101):
    page.set_value(progr, i, fire_and_forget=True)
    time.sleep(0.1)


page.wait_close()