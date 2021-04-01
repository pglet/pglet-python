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
        self.checkbox = Checkbox(value=False, label=name, onchange=self.checkbox_changed)
        self.edit_name = Textbox(width='100%')
        self.display_control = Stack(horizontal=True, horizontal_align='space-between',
                vertical_align='center', controls=[
                self.checkbox,
                Stack(horizontal=True, gap='0', controls=[
                    Button(icon='Edit', title='Edit todo', onclick=self.edit_clicked),
                    Button(icon='Delete', title='Delete todo', onclick=self.delete_clicked)]),
                ])
        
        #stack displayed when edit is clicked 
        self.edit_control = Stack(visible=False, horizontal=True, horizontal_align='space-between',
                vertical_align='center', controls=[
                self.edit_name, Button(text='Save', onclick=self.save_clicked)
                ])
        self.view = Stack(controls=[self.display_control, self.edit_control])

    def edit_clicked(self, e):
        self.edit_name.value = self.checkbox.label
        self.display_control.visible = False
        self.edit_control.visible = True
        self.app.update()

    def save_clicked(self, e):
        self.checkbox.label = self.edit_name.value
        self.display_control.visible = True
        self.edit_control.visible = False
        self.app.update()

    def delete_clicked(self, e):
        self.app.delete_task(self)
    
    def checkbox_changed(self, e):
        if (self.checkbox.value and self.app.tabs.value=='active') or (self.checkbox.value==False and self.app.tabs.value=='completed'):
            self.view.visible = False
        self.app.update()

class TodoApp():
    def __init__(self, page):
        self.tasks = []
        self.page = page
        self.new_task = Textbox(placeholder='Whats needs to be done?', width='100%')
        self.tasks_stack = Stack()
        self.items_left = Text('0 active items')
        self.tabs = Tabs(value='all', onchange=self.tabs_changed, tabs=[
                Tab(text='all'),
                Tab(text='active'),
                Tab(text='completed')])
        self.view = Stack(width='70%', controls=[
            Text(value='Todos', size='large', align='center'),
            Stack(horizontal=True, controls=[
                self.new_task,
                Button(id='add', primary=True, text='Add', onclick=self.add_clicked)]),
            Stack(gap=25, controls=[
                self.tabs,
                self.tasks_stack,
                Stack(horizontal=True, horizontal_align='space-between', vertical_align='center', controls=[
                    self.items_left,
                    Button(id='clear_completed', text='Clear completed', onclick=self.clear_clicked)
                ])
            ])
        ])

    def update(self):
        count = 0
        for task in self.tasks:
            if task.checkbox.value == False:
                count += 1
        self.items_left.value = f"{count} active items left"
        self.page.update()

    def delete_task(self, task):
        self.tasks.remove(task)
        self.tasks_stack.controls.remove(task.view)
        self.update()
    
    def add_clicked(self, e):
        task_name = self.new_task.value
        task = Task(self, task_name)
        self.tasks.append(task)
        self.tasks_stack.controls.append(task.view)
        self.new_task.value = ''
        self.update()       
    
    def clear_clicked(self, e):
        for task in self.tasks[:]:
            if task.checkbox.value == True:
                self.delete_task(task)

    def tabs_changed(self, e):
        for task in self.tasks:
            task.view.visible = e.data=='all' or (e.data=='active' and task.checkbox.value==False) or (e.data=='completed' and task.checkbox.value)
        self.update()

def main(page):
    app = TodoApp(page)
    page.title = "Python Todo with Pglet"
    page.update()
    page.clean(True)
    page.add(app.view)

#pglet.app("todo-app", target = main)
page = pglet.page("todo-app")
main(page)

input("Press Enter to exit...")