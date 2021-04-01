import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Grid, Column, Textbox

page = pglet.page("index", no_window = True)
page.clean(force=True)
page.title = "Grid test"
page.update()

class Contact():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

grid = Grid(selection='multiple', compact=True, header_visible=True, shimmer_lines=1, columns=[
    Column(field_name="first_name", name='First name', icon='mail', icon_only=True,
    sortable='True', sort_field='sort field name', sorted='false', resizable=False, min_width=100, max_width=200),
    Column(field_name="last_name", name='Last name', template_controls=[
        Textbox(value="{last_name}")
    ])
], items=[
    Contact(first_name='John', last_name='Smith'),
    Contact(first_name='Jack', last_name='Brown'),
    Contact(first_name='Alice', last_name='Fox')
])

page.add(grid)

input("Press Enter to exit...")