import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Button, Stack, Textbox, SearchBox, Icon

def main(page):
    global icon_names
    page.update(Page(title="Icon Browser"))
    page.clean()

    def search_icons(search_name):
        found_icon_names = []
        if search_name==None:
            found_icon_names = icon_names
        else:
            for icon_name in icon_names:
                if search_name.lower() in icon_name.lower():
                    found_icon_names.append(icon_name)
        return found_icon_names

    def searchbox_changed(e):
        search_name = page.get_value('searchbox')
        stack_controls = get_stack_controls(search_name)
        page.replace(stack_controls, to=result_stack)
        #print('Seachbox changed to ' + search_name)

    def enter_clicked(e):
        search_name = page.get_value('searchbox')
        stack_controls = get_stack_controls(search_name)
        page.replace(stack_controls, to=result_stack)
        #print('Seachbox changed to ' + search_name)
            
    #add stack controls each with Icon and Text
    def get_stack_controls(search_name):
        stack_controls = []
        found_icon_names = search_icons(search_name)
        for icon_name in found_icon_names:
            s = Stack(controls=[
                Icon(name = icon_name),
                Text(value = icon_name)
            ])
            stack_controls.append(s)
        return stack_controls
        
    stack_controls = get_stack_controls(None)

    '''
      pglet_send "add
    searchbox id=search placeholder='Search icons'
    stack id=result horizontal wrap
  "

  pglet_send "add to=result
    stack horizontalAlign=center verticalAlign=center width=100 height=100 border='solid 1px #eee' borderRadius=3
      icon name=Shop size=40 color='#555'
      text value='Shop' size=small
    stack horizontalAlign=center verticalAlign=center width=100 height=100 border='solid 1px #eee' borderRadius=3
      icon name=Installation size=40 color='#555'
      text value='Installation' size=small
  "
    '''
        
    result_stack = Stack(horizontal=True, wrap=True, horizontal_align='center', vertical_align='center', controls=stack_controls)
    page.add(SearchBox(id='searchbox', onchange=searchbox_changed, onsearch=enter_clicked, on_change=True), result_stack)

    page.wait_close()

# read list of icon names from file
file_path = 'C:/Projects/Python/pglet_samples/fluent-icons-clean.txt'
input_file = open(file_path, 'r')   
icon_names = []
for line in input_file:
    line=line.strip()
    icon_names.append(line)
input_file.close()

pglet.app("icon-browser-app", target = main)

#pglet.app("inesa-counter-app", target = main, web = True)