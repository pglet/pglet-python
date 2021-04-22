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
    multiline_textboxes(),

    Text("Underlined and borderless Textboxes", size="xLarge"),
    underlined_borderless_textboxes(), 

    Text("TextField with prefix and/or suffix", size="xLarge"),
    suffix_prefix_textboxes()
  ])

def basic_textboxes():
  return Stack(controls=[
    Stack(gap=25, horizontal=True, controls=[
      Textbox(label='Standard'),
      Textbox(label='Disabled', disabled=True)
    ]),
    Stack(gap=25, horizontal=True, controls=[
      Textbox(label='Read-only', read_only=True),  
      Textbox(label="With placeholder", placeholder='Please enter text here')
    ]),
    Stack(gap=25, horizontal=True, controls=[
      Stack(controls=[
         Textbox(label='Required:', required=True),
         Textbox(required=True) 
      ]),
      Textbox(label="With error message", error_message='Error message')
    ]),
    Stack(gap=25, horizontal=True, controls=[
      Textbox(label='With an icon', icon='Emoji2'), #need icon property
      Textbox(label='Password with reveal button', password=True)
    ]),
    Stack(gap=25, horizontal=True, controls=[
      textbox_with_onchange()
    ])

  ])

def textbox_with_onchange():
    
    def textbox_changed(e):
      displayed_text.value = entered_text.value
      stack.update()

    entered_text = Textbox(label='With onchange event', on_change=textbox_changed)
    displayed_text = Text()
    stack = Stack(controls=[entered_text, displayed_text])
    return stack

def multiline_textboxes():
  return Stack(controls=[
    Stack(gap=25, horizontal=True, controls=[
      Textbox(label='standard', multiline=True),
      Textbox(label='disabled', multiline=True, disabled=True)
    ]),
    Stack(gap=25, horizontal=True, controls=[
      Textbox(label='With auto adjusted height', multiline=True, auto_adjust_height=True) #need auto-adjusted height property
    ])
  ])

def underlined_borderless_textboxes():
  return Stack(controls=[
    Stack(gap=25, controls=[
      Textbox(label='Underlined', underlined=True, placeholder='Enter text here'),
      Textbox(label='Borderless', borderless=True, placeholder='Enter text here')
    ])
  ])

def suffix_prefix_textboxes():
  return Stack(controls=[
    Stack(gap=25, horizontal=True, controls=[
      Textbox(label='With prefix', prefix='https://'),
      Textbox(label='With suffix', suffix='.com')
    ]),
    Stack(horizontal=True, controls=[
      Textbox(label='With prefix and suffix', prefix='https://', suffix='.com')
    ])
  ])

def main(page):

    page.title = "Textbox control samples"
    page.update()
    #page.clean(True)

    page.add(textboxes())

pglet.app("textbox-control-samples", target = main)

input("Press Enter to exit...")