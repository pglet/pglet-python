import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text, Toggle

def toggles(page):
  return Stack(controls=[
        Text("Toggles", size="xLarge"),
        Toggle(label='Enabled and checked', value=True),
        Toggle(label='Enabled and unchecked'),
        Toggle(disabled=True, label='Disabled and checked', value=True),
        Toggle(disabled=True, label='Disabled and unchecked'),
        Toggle(inline=True, label='With inline label', on_text='On', off_text='Off'),
        Toggle(disabled=True, inline=True, label='Disabled with inline label', on_text='On', off_text='Off'),
        Toggle(inline=True, label='With inline label and without onText and offText'),
        Toggle(disabled=True, inline=True, label='Disabled with inline label and without onText and offText'),
        toggle_with_on_change(page=page)
        ])

def toggle_with_on_change(page):
    
    def toggle_changed(e):
      if t.value:
        # Dark theme
        page.theme = 'dark'
      else:
        page.theme = 'light'
      
      page.update()

    t = Toggle(label="With Change event", on_text="Dark theme", off_text="Light theme", value=False, on_change=toggle_changed)
    return t

def main(page):
    
    page.title = "Toggle control samples"
    page.update()
    page.add(toggles(page))

pglet.app("python-toggle", target=main)