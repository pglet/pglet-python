import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text, Textbox

def textboxes():
  return Stack(gap=20, controls=[
    Text("Basic textboxes", size="xLarge"),
    basic_textboxes(),
    
    Text("Multiline textboxes", size="xLarge"),
    multiline_textboxes()  
  ])

def basic_textboxes():
  return Stack(controls=[
    Stack(horizontal=True, controls=[
      Textbox(label='Standard'),
      Textbox(label='Disabled', disabled=True)
    ]),
    Stack(horizontal=True, controls=[
      Textbox(label='Read-only'), #need to add read-only property  
      Textbox(label="With placeholder", placeholder='Please enter text here')
    ]),
    Stack(horizontal=True, controls=[
      Textbox(label='Required *'), #need to add required property. How to dispay * in red?
      Textbox(label="With error message", error_message='Error message')
    ]),
    Stack(horizontal=True, controls=[
      Textbox(label='With an icon'), #need icon property
      Textbox(label='Password with reveal button', password=True)
    ]),
    Stack(horizontal=True, controls=[
      textbox_with_onchange()
    ])

  ])

def textbox_with_onchange():
    
    def textbox_changed(e):
      print(e)
      displayed_text.value = entered_text.value
      stack.update()

    entered_text = Textbox(label='With onchange event', on_change=textbox_changed)
    displayed_text = Text()
    stack = Stack(controls=[entered_text, displayed_text])
    return stack

def multiline_textboxes():
  return Stack(controls=[
    Stack(horizontal=True, controls=[
      Textbox(label='standard', multiline=True),
      Textbox(label='disabled', multiline=True, disabled=True)
    ]),
    Stack(horizontal=True, controls=[
      Textbox(label='Non-resizable', multiline=True), #need non-resizable property
      Textbox(label='With auto adjusted height', multiline=True) #need auto-adjusted height property
    ])
  ])

def main(page):

    page.title = "Textbox control samples"
    page.update()
    #page.clean(True)

    page.add(textboxes())

pglet.app("textbox-control-samples", target = main)

input("Press Enter to exit...")