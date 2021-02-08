import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import time
import pglet
from pglet import Page, Text, Textbox, Button, Progress

page = pglet.page("index")
page.update(Page(title="Hello, pglet!"))
page.clean()
page.add(Text(value='Hello', align='right', width='100%'))

page.wait_close()