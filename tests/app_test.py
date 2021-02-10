import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import time
import pglet
from pglet import Page, Text, Textbox, Button, Progress, Icon, Link, Toggle, Message, MessageButton
#from pglet.message import MessageButton

def link_click(event):
    print('This link is clicked!')

def toggle_change(event):
    print('This toggle is changed!')

def message_dismissed(event):
    print('This message is dismissed!')

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


page.wait_close()