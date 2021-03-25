import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Button, Stack, Textbox, Checkbox, Tabs, Tab

page = pglet.page("index", no_window = True)

page.clean(force=True)

page.title = "Counter"
page.update()

txtNum = Textbox(value = '0', align = 'right')

def on_click(e):
    try:
        count = int(txtNum.value)
        
        if e.data == "+":
            count += 1
        elif e.data == "-":
            count -= 1
        
        txtNum.value = count
        txtNum.error_message = ""

    except ValueError:
        txtNum.error_message = "Please enter a number"
    
    page.update()

stack = Stack(horizontal = True, controls=[
        Button('-', onclick=on_click, data='-'),
        txtNum,
        Button('+', onclick=on_click, data='+'),
    ])

page.add(stack)

stack2 = Stack(width='70%', controls=[
        Text(value='Todos', size='large', align='center'),
        Stack(horizontal=True, controls=[
            Textbox(id='new_task', placeholder='Whats needs to be done?', width='100%'),
            Button(id='add', primary=True, text='Add')]),
        Stack(gap=25, controls=[
            Tabs(tabs=[
                Tab(text='all'),
                Tab(text='active'),
                Tab(text='completed')]),
            Stack(horizontal=True, horizontal_align='space-between', vertical_align='center', controls=[
                Text(id='items_left', value='0 items left'),
                Button(id='clear_completed', text='Clear completed')
            ])
        ])
    ])

page.add(stack2)

chk = Checkbox("Check it!", id="check1")
page.add(chk)

chk.label = "Check it, again!"
page.update()

# stack.controls.pop(0)
# page.update()

input("Press Enter to exit...")