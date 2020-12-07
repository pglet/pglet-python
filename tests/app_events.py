import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import time
import pglet
from pglet import Text, Textbox, Button, Progress

page = pglet.page("index", no_window=True)
page.clean()

txt = Textbox(label="Your name")
btn = Button(text="Say hello", primary=True)
page.add(txt, btn)

while True:
    e = page.wait_event()
    print(e)

    if e.target == btn.id and e.name == "click":
        name = page.get_value(txt)

        if name == "":
            txt.error_message = "Name cannot be blank"
            btn.text = "Say it again!"
            page.update(txt, btn)
            continue

        page.remove(btn)
        page.add(Text(value=f'Hello, {name}!'), at=0)

        prg = page.add(Progress(label="Doing something..."))
        for i in range(1, 11):
            page.set_value(prg, i * 10)
            time.sleep(1)

        break