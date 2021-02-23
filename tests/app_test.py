import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import time
import pglet
from pglet import Page, Text, Textbox, Button, Progress, Icon, Link, Toggle, Message, MessageButton, Checkbox, ChoiceGroup, Dropdown
from pglet import choicegroup
from pglet import dropdown
from pglet import nav
from pglet import Nav, SearchBox, Slider, SpinButton, Tabs, Tab, Dialog, Panel, Toolbar
from pglet import Grid, Column
from pglet import VerticalBarChart, P
from pglet import Image
from pglet import toolbar
from pglet import button

class Contact():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

def link_click(event):
    print('This link is clicked!')

def toggle_change(event):
    print('This toggle is changed!')

def message_dismissed(event):
    print('This message is dismissed!')

def checkbox_changed(event):
    print('This checkbox is changed!')

def choicegroup_changed(event):
    print('This choicegroup is changed!')

def dropdown_changed(event):
    print('This dropdown is changed!')

def navitem_changed(event):
    print('This navitem is changed!')

def navitem_expanded(event):
    print('This navitem is expanded!')

def navitem_collapsed(event):
    print('This navitem is collapsed!')

def searchbox_changed(event):
    print('This searchbox is changed!')

def slider_changed(event):
    print('This slider is changed!')

def spinbutton_changed(event):
    print('This spinbutton is changed!')

def tabs_changed(event):
    print('This tabs is changed!')

def button_clicked(event):
    print('This button is clicked!')

def item_clicked(event):
    print('This item is clicked!')

page = pglet.page("index")
page.update(Page(title="Hello, pglet!"))
page.clean()

b = Button(primary=False, compound=False, action=False, toolbar=True, split=False, text='This is text', 
    secondary_text='This is secondary text', url='https://google.com', new_window=True, title='This is title',
    icon='Mail', icon_color='red', data='data', onclick=button_clicked, items=[
        button.Item(text='Item1 text', secondary_text='Item1 secondary text', url='https://google.com', new_window=False,
        icon='Mail', icon_color='blue', icon_only=True, split=False, divider=False, onclick=item_clicked, items=[
            button.Item('Item1Item1'),
            button.Item('Item1Item2')
        ]),
        button.Item(text='Item2 text')
    ])
page.add(b)

i = Image(src='https://www.w3schools.com/css/img_5terre.jpg', alt='This is image', title='This is title',
 maximize_frame=False)
page.add(i)

page.add(Text(value='C:\\He\nllo', align='right', width='100%', nowrap=True, size='small'))
page.add(Icon(name='Mail', color='green', size='large'))
page.add(Link(value='Visit google', url='https://google.com', pre=True, align='right', width='100', size='large1'))
page.add(Link(value='Start action', url=None, new_window=False, onclick=link_click))
page.add(Toggle(value=True, label='This is toggle', on_text='On text', off_text='Off text', 
    inline=True, onchange=toggle_change))

page.add(Message(value='This is message', dismiss=True, ondismiss=message_dismissed, buttons=[
    MessageButton(text='Yes, I agree', action='Yes'),
    MessageButton(text='No, I disagree', action='No')
]))

page.add(Checkbox(value=True, label='I am a human', box_side='start', data='data to pass', onchange=checkbox_changed))

page.add(ChoiceGroup(value='colour', label='Select a colour:', data='data to pass', options=[
    choicegroup.Option(key='Green'),
    choicegroup.Option(key='Yellow')], 
    onchange=choicegroup_changed))

page.add(Dropdown(id='dd1', label='Choose your weapon', options=[
    dropdown.Option('Sword'),
    dropdown.Option('Word'),
    dropdown.Option('Poison')],
    onchange=dropdown_changed))
    
page.add(Nav(id='n1', value='n1', items=[
    nav.Item(key='Item1', items=[
        nav.Item('item1.1', items=
            [nav.Item(key='item1.1.1', icon='mail', icon_color='green', url='https://google.com', expanded=True, new_window=True),
            nav.Item('item1.1.2')]),
        nav.Item('item1.2')
    ]),
    nav.Item('Item2'),
    nav.Item('Item3'),],
    onchange=navitem_changed, onexpand=navitem_expanded, oncollapse=navitem_collapsed))

page.add(SearchBox(value='', placeholder='search for something', underlined=True, icon='mail', 
    icon_color='red', data='data', on_change=True, onchange=searchbox_changed))

page.add(Slider(value=1, label='To what extend you agree', min=0, max=10, step=1, 
    show_value=True, value_format='current_value is {value}', vertical=False, onchange=slider_changed))

page.add(SpinButton(value=1, label='Level of satisfaction', min=0, max=10, step=1, 
    icon='mail', width=200, onchange=spinbutton_changed))

page.add(Tabs(id='t1', value='Tabs101', tabs=[
    Tab(text='Tab1', controls=[
        Button(text='hello')
    ]),
    Tab(text='Tab2', controls=[
        Text(value='this is text')
    ]),
    Tab(text='Tab3')],
    onchange=tabs_changed))

d = Dialog(title='Hello', open=True, controls=[
    Text(value='Are you sure?')
], footer=[
    Button(text='OK'),
    Button(text="Cancel")
])

d.footer.id = "myfooter"

#page.add(d)

id = d.footer.id 
print(id)

g = Grid(columns=[
    Column(field_name="first_name", name='First name'),
    Column(field_name="last_name1", name='Last name')
], items=[
    Contact(first_name='Inesa', last_name='Fitsner'),
    Contact(first_name='Fiodar', last_name='Fitsner')
])

#page.add(g)

p = Panel(title='Hello', open=True, controls=[
    Text(value='Are you sure?')
], footer=[
    Button(text='OK'),
    Button(text="Cancel")
])

#page.add(p)

t = Toolbar(items=[
    toolbar.Item(text='Are you sure?')
], overflow=[
    toolbar.Item(text='OK'),
    toolbar.Item(text="Cancel")
], far=[
    toolbar.Item(text='far')
])

#page.add(t)

vbc = VerticalBarChart(x_type='number', data=[
    P(x='1', y=100),
    P(x='80', y=200), 
    P(x='100', y=300),
])

page.add(vbc)

#page.wait_close()