import os

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Textbox, Button, Checkbox

def main(page):

    page.title = "ToDo App"
    page.horizontal_align = 'center'
    page.update() # needs to be called every time "page" control is changed
    
    def add_clicked(e):
        tasks_view.controls.append(Checkbox(label=new_task.value))
        tasks_view.update()

    new_task = Textbox(placeholder='Whats needs to be done?', width='100%')
    tasks_view = Stack()

    page.add(Stack(width='70%', controls=[
        Stack(horizontal=True, controls=[
            new_task,
            Button('Add', on_click=add_clicked)
        ]),
        tasks_view
    ]))

pglet.app("todo-app", target=main)