import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text, Toolbar, Message
from pglet import toolbar


def toolbars(page):

  def item_clicked(e):
    page.controls.insert(0, Message(value=f'Menu item "{e.control.text}" was clicked', dismiss=True))
    page.update()

  standard_toolbar = Toolbar(items=[
        toolbar.Item(text='New', icon='Add', items=[
            toolbar.Item(text='Email message', icon='Mail', on_click=item_clicked),
            toolbar.Item(text='Calendar event', icon='Calendar', on_click=item_clicked)
            ]),  
        toolbar.Item(text='Share', icon='Share', split=True, items=[
            toolbar.Item(text='Share to Twitter', on_click=item_clicked),
            toolbar.Item(text='Share to Facebook', on_click=item_clicked),
            toolbar.Item(text='Share to Somewhere', disabled=True, on_click=item_clicked),
            toolbar.Item(text='Share to Email', data='sharetoemail', items=[
                toolbar.Item(text='Share to Outlook', on_click=item_clicked),
                toolbar.Item(text='Share to Gmail', on_click=item_clicked)
            ])
        ]),
        toolbar.Item(text='To to Google', icon='Globe', url='https://google.com', new_window=True, secondary_text='New window')
        ], 
        overflow=[
            toolbar.Item(text='Item 1', icon='Shop', on_click=item_clicked),
            toolbar.Item(text='Item 2', icon='Airplane', on_click=item_clicked)
        ], 
        far=[
            toolbar.Item(text='Grid view', icon='Tiles', icon_only=True, on_click=item_clicked),
            toolbar.Item(text='Info', icon='Info', icon_color='green', icon_only=True, on_click=item_clicked)
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

  return Stack(gap=30, controls=[
      Stack(controls=[
          Text("Standard toolbar with Click events", size="xLarge"),
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
    page.add(toolbars(page))

pglet.app("toolbar-control-samples", target = main)

input("Press Enter to exit...")