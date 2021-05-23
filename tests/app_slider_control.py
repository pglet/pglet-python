import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text, Slider

def sliders():
  return Stack(width='50%', controls=[
    Stack(controls=[
        Text("Horizontal sliders", size="xLarge"),
        Slider(label='Default slider'),
        Slider(label='Default disabled slider', disabled=True),
        Slider(label='Slider with value', show_value=True, value=4),
        Slider(label='Slider with formatted value', show_value=True, min=0, max=100, value=40, value_format='{value}%'),
        Slider(show_value=True, label='Origin from zero', min=-5, max=15, step=1, value=-2),
        slider_with_on_change()
        ]),
    Text("Vertical sliders", size='xLarge'),
    Stack(horizontal=True, height='200px', controls=[
        Slider(vertical=True, label='Default slider'),
        Slider(vertical=True, label='Default disabled slider', disabled=True),
        Slider(vertical=True, label='Slider with value', show_value=True, value=4),
        Slider(vertical=True, label='Slider with formatted value', show_value=True, min=0, max=100, value=40, value_format='{value}%'),
        Slider(vertical=True, show_value=True, label='Origin from zero', min=-5, max=15, step=1, value=-2)
    ])
  ]) 

def slider_with_on_change():
    
    def slider_changed(e):
      s.data += 1
      t.value = f"Slider changed to {s.value}"
      stack.update()

    s = Slider('Slider with Change event', on_change=slider_changed, data=0)
    t = Text()
    stack = Stack(controls=[s, t])
    return stack

def main(page):

    page.title = "Slider control samples"
    page.update()
    page.add(sliders())

pglet.app("slider-control-samples", target = main, local=True)

input("Press Enter to exit...") 