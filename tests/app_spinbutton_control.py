import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text, SpinButton

def spinbuttons():
  return Stack(gap=20, controls=[
    Stack(controls=[
        Text("Spinbuttons", size="xLarge"),
        SpinButton(label='Basic SpinButton:', min=0, max=100, step=1, value=0),
        SpinButton(disabled=True, label='Disabled SpinButton:', min=0, max=100, step=1, value=0),
        SpinButton(icon='IncreaseIndentLegacy', label='SpinButton with icon:', min=0, max=100, step=1, value=0),
        spinbutton_with_on_change()
        ])
  ]) 

def spinbutton_with_on_change():
    
    def spinbutton_changed(e):
      s.data += 1
      t.value = f"Spinbutton changed to {int(s.value)}"
      stack.update()

    s = SpinButton('SpinButton with Change event', on_change=spinbutton_changed, data=0)
    t = Text()
    stack = Stack(controls=[s, t])
    return stack

def main(page):

    page.title = "SpinButton control samples"
    page.update()
    page.add(spinbuttons())

pglet.app("spinbutton-control-samples", target = main)

input("Press Enter to exit...") 