import os

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Textbox, Button, Checkbox

class TodoApp():
    def __init__(self):
        self.new_task = Textbox(placeholder='Whats needs to be done?', width='100%')
        self.tasks_view = Stack()

        # application's root control (i.e. "view") containing all other controls
        self.view = Stack(width='70%', controls=[
            Stack(horizontal=True, on_submit=self.add_clicked, controls=[
                self.new_task,
                Button('Add', on_click=self.add_clicked)
            ]),
            self.tasks_view
        ])

    def add_clicked(self, e):
        self.tasks_view.controls.append(Checkbox(label=self.new_task.value))
        self.tasks_view.update()

def main(page):
    page.title = "ToDo App"
    page.horizontal_align = 'center'
    page.update()

    # create application instance
    app = TodoApp()

    # add application's root control to the page
    page.add(app.view)

pglet.app("todo-app", target=main)