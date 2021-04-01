import os

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Checkbox, Button, Stack, Textbox, Tabs, Tab

class Task():
    def __init__(self, app, name):
        self.app = app
        self.display_task = Checkbox(value=False, label=name)
        self.view = self.display_task

class TodoApp():
    def __init__(self):
        self.tasks = []
        self.new_task = Textbox(placeholder='Whats needs to be done?', width='100%')
        self.tasks_view = Stack()
        self.filter = Tabs(value='all', onchange=self.tabs_changed, tabs=[
                Tab(text='all'),
                Tab(text='active'),
                Tab(text='completed')])
        self.view = Stack(width='70%', controls=[
            Stack(horizontal=True, controls=[
                self.new_task,
                Button(primary=True, text='Add', onclick=self.add_clicked)]),
            Stack(gap=25, controls=[
                self.filter,
                self.tasks_view
            ])
        ])

    def update(self):
        count = 0
        status = self.filter.value
        for task in self.tasks:
            task.view.visible = status == 'all' or (status == 'active' and task.display_task.value == False) or (status == 'completed' and task.display_task.value)
            if task.display_task.value == False:
                count += 1
        self.view.update()
    
    def add_clicked(self, e):
        task = Task(self, self.new_task.value)
        self.tasks.append(task)
        self.tasks_view.controls.append(task.view)
        self.new_task.value = ''
        self.update()

    def tabs_changed(self, e):
        self.update()

def main(page):
    page.title = "Python Todo with Pglet"
    page.update()
    page.clean(True)

    app1 = TodoApp()
    page.add(app1.view)

    app2 = TodoApp()
    page.add(app2.view)

#pglet.app("todo-app", target = main)
page = pglet.page("todo-app", no_window=True)
main(page)

input("Press Enter to exit...")