import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Button, Stack, Textbox, SearchBox, Checkbox, Tabs, Tab, Icon

page = pglet.page("index", no_window = True)

page.clean(force=True)

page.title = "Perf tuning"
page.update()

items = Stack(id="icons", horizontal=True, wrap=True)

stack = Stack(id="container", controls=[
    SearchBox(),
    items
])

for n in range(1000):
    s = Stack(horizontal_align='center', vertical_align='center', width=100, height=100, 
        border='solid 1px #eee', border_radius='3', controls=[
        Icon(name = "Favicon", size='40', color='#555'),
        Text(value = f'C{n}', size='small')
    ])

    #items.controls.append(Text(f'C{n}'))
    items.controls.append(s)

#page.add(stack)

chk = Checkbox("Check, check!")

page.add(
    SearchBox(onsearch=lambda e: print(chk.value)),
    chk,
    items)

input("Press Enter to exit...")