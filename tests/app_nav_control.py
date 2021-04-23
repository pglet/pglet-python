import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text, Nav, Message
from pglet import nav

def navs(page):

  nav1 = None

  def menu_item_expanded(e):
    page.controls.insert(0, Message(value=f'Menu item "{e.data}" was expanded', dismiss=True))
    page.update()

  def menu_item_collapsed(e):
    page.controls.insert(0, Message(value=f'Menu item "{e.data}" was collapsed', dismiss=True))
    page.update()

  def menu_item_changed(e):
    page.controls.insert(0, Message(value=f'Menu item was changed to "{nav1.value}"', dismiss=True))
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
      Stack(controls=[
          Text("Nav with groups and Expand, Collapse and Change events", size="xLarge"),
          nav1
      ]),
      Stack(controls=[
          Text("Nav without groups", size="xLarge"),
          nav2
      ])
  ])


'''

def toggle_with_on_change(page):
    
    def toggle_changed(e):
      if t.value:
        # Dark theme
        page.theme_background_color = '#262626'
        page.theme_primary_color = '#3ee66d'
        page.theme_text_color = '#edd2b7'
      else:
        page.theme_background_color = ''
        page.theme_primary_color = ''
        page.theme_text_color = ''
      
      page.update()

    t = Toggle(label="With Change event", on_text="Dark theme", off_text="Light theme", value=False, on_change=toggle_changed)
    return t
'''

def main(page):
    
    page.title = "Nav control samples"
    page.update()
    page.add(navs(page))

pglet.app("nav-control-samples", target = main)

input("Press Enter to exit...") 