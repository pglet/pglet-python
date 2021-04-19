import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from typing import get_type_hints
from dataclasses import dataclass
import pglet
from pglet import Grid, Column, Textbox, Checkbox, Button

page = pglet.page("index")
page.clean(force=True)
page.title = "Grid test"
page.update()

class Contact():
    def __init__(self, first_name: str, last_name: str, employee: int):
        self.first_name = first_name
        self.last_name = last_name
        self.employee = employee

print(get_type_hints(Contact))

def display_items(e):
    for item in grid.items:
        print(item.first_name, item.last_name, item.employee)

n = 1
def add_item(e):
    global n
    grid.items.pop(0)
    grid.items.append(Contact(first_name=f'First {n}', last_name=f'Last {n}', employee=False))
    grid.update()
    n += 1

def grid_selected(e):
    print(e.control.selected_items)

grid = Grid(selection='multiple', compact=True, header_visible=True, shimmer_lines=1, columns=[
    Column(field_name="first_name", name='First name', icon='mail', icon_only=True,
    sortable='True', sort_field='sort field name', sorted='false', resizable=False, min_width=100, max_width=200),
    Column(field_name="last_name", name='Last name', template_controls=[
        Textbox(value="{last_name}")
    ]),
    Column(field_name="employee", name='Is employee', template_controls=[
        Checkbox(value_field="employee")
    ])    
], items=[
    Contact(first_name='John', last_name='Smith', employee=False),
    Contact(first_name='Jack', last_name='Brown', employee=True),
    Contact(first_name='Alice', last_name='Fox', employee=False)
], on_select=grid_selected)

btn = Button("Show items", on_click=display_items)
btnAdd = Button("Add item", on_click=add_item)

page.add(grid, btn, btnAdd)

input("Press Enter to exit...")