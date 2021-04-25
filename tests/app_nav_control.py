import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text, Nav, Message
from pglet import nav

def navs(page):

  message = Message(dismiss=True, visible=False)


  def menu_item_expanded(e):
    message.visible = True
    message.value = f'Menu item "{e.data}" was expanded'
    page.update()

  def menu_item_collapsed(e):
    message.visible = True
    message.value = f'Menu item "{e.data}" was collapsed'
    page.update()

  def menu_item_changed(e):
    message.visible = True
    message.value = f'Menu item was changed to "{e.control.value}"'
    page.update()

  nav1 = Nav(on_collapse=menu_item_collapsed, on_expand=menu_item_expanded, on_change=menu_item_changed, items=[
              nav.Item(text='Actions', items=[
                  nav.Item(expanded=True, text='New', items=[
                      nav.Item(key='email', text='Email message', icon='Mail'),
                      nav.Item(key='calendar', text='Calendar event', icon='Calendar', icon_color='salmon')
                  ]),
                  nav.Item(text='Share', items=[
                      nav.Item(disabled=True, key='share', text='Share to Facebook', icon='Share'),
                      nav.Item(key='twitter', text='Share to Twitter')
                  ]),
                  nav.Item(text='Links', items=[   
                      nav.Item(text='Pglet website', icon='NavigateExternalInline', url='https://pglet.io', new_window=True),
                      nav.Item(text='Google website', icon='NavigateExternalInline', url='https://google.com', new_window=True) 
                  ])
                ])
            ])

  nav2 = Nav(items=[
              nav.Item(items=[
                nav.Item(expanded=True, text='New', items=[
                    nav.Item(key='email', text='Email message', icon='Mail'),
                    nav.Item(key='calendar', text='Calendar event', icon='Calendar'),
                    nav.Item(text='More options', items=[
                       nav.Item(key='option', text='Web component', icon='WebComponents')
                    ])
                ]),
                nav.Item(expanded=True, text='Share', items=[
                    nav.Item(key='facebook', text='Share on Facebook', icon='Share'),
                    nav.Item(key='twitter', text='Share to Twitter', icon='Share')
                ])

              ])
            ])

  return Stack(gap=30, controls=[
      message,
      Stack(controls=[
          Text("Nav with groups and Expand, Collapse and Change events", size="xLarge"),
          nav1
      ]),
      Stack(controls=[
          Text("Nav without groups", size="xLarge"),
          nav2
      ])
  ])

def main(page):
    
    page.title = "Nav control samples"
    page.update()
    page.add(navs(page))

pglet.app("nav-control-samples", target = main)

input("Press Enter to exit...") 