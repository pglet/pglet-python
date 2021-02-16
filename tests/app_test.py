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
from pglet import Nav, SearchBox

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

page = pglet.page("index")
page.update(Page(title="Hello, pglet!"))
page.clean()
page.add(Text(value='Hello', align='right', width='100%', nowrap=True, size='small'))
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

page.wait_close()