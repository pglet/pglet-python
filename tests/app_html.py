import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Html

page = pglet.page("html-test")
page.clean()

page.title = "Html Test"
page.update()

page.add(Html("<b>Hello, world!</b>"))
