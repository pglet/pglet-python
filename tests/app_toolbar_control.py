import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text, Toolbar, Message
from pglet import toolbar

standard_toolbar = Toolbar(items=[
        toolbar.Item(text='New', icon='Add', items=[
            toolbar.Item(text='Email message', icon='Mail'),
            toolbar.Item(text='Calendar event', icon='Calendar')
            ]),  
        toolbar.Item(text='Share', icon='Share', split=True, items=[
            toolbar.Item(text='Share to Twitter'),
            toolbar.Item(text='Share to Facebook'),
            toolbar.Item(text='Share to Somewhere', disabled=True),
            toolbar.Item(text='Share to Email', data='sharetoemail', items=[
                toolbar.Item(text='Share to Outlook'),
                toolbar.Item(text='Share to Gmail')
            ])
        ]),
        toolbar.Item(text='To to Google', icon='Globe', url='https://google.com', new_window=True, secondary_text='New window')
        ], 
        overflow=[
            toolbar.Item(text='Item 1', icon='Shop'),
            toolbar.Item(text='Item 2', icon='Airplane')
        ], 
        far=[
            toolbar.Item(text='Grid view', icon='Tiles', icon_only=True),
            toolbar.Item(text='Info', icon='Info', icon_color='green', icon_only=True)
    ])

inverted_toolbar = Toolbar(inverted=True, items=[
        toolbar.Item(text='New', icon='Add', items=[
            toolbar.Item(text='Email message', icon='Mail'),
            toolbar.Item(text='Calendar event', icon='Calendar')
            ]),  
        toolbar.Item(text='Share', icon='Share', split=True, items=[
            toolbar.Item(text='Share to Twitter'),
            toolbar.Item(text='Share to Facebook'),
            toolbar.Item(text='Share to Somewhere', disabled=True),
            toolbar.Item(text='Share to Email', data='sharetoemail', items=[
                toolbar.Item(text='Share to Outlook'),
                toolbar.Item(text='Share to Gmail')
            ])
        ]),
        toolbar.Item(text='To to Google', icon='Globe', url='https://google.com', new_window=True, secondary_text='New window')
        ], 
        overflow=[
            toolbar.Item(text='Item 1', icon='Shop'),
            toolbar.Item(text='Item 2', icon='Airplane')
        ], 
        far=[
            toolbar.Item(text='Grid view', icon='Tiles', icon_only=True),
            toolbar.Item(text='Info', icon='Info', icon_color='green', icon_only=True)
    ])

def toolbar(page):

  def menu_item_clicked(e):
    page.controls.insert(0, Message(value=f'Menu item was changed to "{e.control.text}"', dismiss=True))
    page.update()

  return Stack(gap=30, controls=[
      Stack(controls=[
          Text("Standard toolbar", size="xLarge"),
          standard_toolbar
      ]),
      Stack(controls=[
          Text("Inverted toolbar (for top application menu)", size="xLarge"),
          Stack(bgcolor='magentaLight', controls=[
            inverted_toolbar
          ])          
      ])
  ])

def main(page):
    
    page.title = "Toolbar control samples"
    page.horizontal_align = 'stretch'
    page.update()
    page.add(toolbar(page))

pglet.app("toolbar-control-samples", target = main)

input("Press Enter to exit...")