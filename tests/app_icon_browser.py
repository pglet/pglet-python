import os

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Stack, SearchBox, Icon

def main(page):
    icon_names = load_icon_names()
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

    def enter_clicked(e):
        search_name = page.get_value('searchbox')
        stack_controls = get_stack_controls(search_name)
        page.replace(stack_controls, to=result_stack)
            
    #add stack controls each with Icon and Text
    def get_stack_controls(search_name):
        stack_controls = []
        found_icon_names = search_icons(search_name)
        for icon_name in found_icon_names:
            s = Stack(horizontal_align='center', vertical_align='center', width=100, height=100, 
                border='solid 1px #eee', border_radius='3', controls=[
                Icon(name = icon_name, size='40', color='#555'),
                Text(value = icon_name, size='small')
            ])
            stack_controls.append(s)
        return stack_controls
        
    stack_controls = get_stack_controls(None)
        
    result_stack = Stack(horizontal=True, wrap=True, controls=stack_controls)
    page.add(SearchBox(id='searchbox', onchange=searchbox_changed, onsearch=enter_clicked, on_change=True), result_stack)

    page.wait_close()


# load list of icon names from file
def load_icon_names():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "fluent-icons-clean.txt")
    input_file = open(file_path, 'r')   
    icon_names = []
    for line in input_file:
        line=line.strip()
        icon_names.append(line)
    input_file.close()
    return icon_names

pglet.app("icon-browser-app2", target = main)