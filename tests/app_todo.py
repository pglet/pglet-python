import os

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Checkbox, Button, Stack, Textbox, Tabs, Tab

class Task():
    def __init__(self, app, id, name):
        self.app = app
        self.id = str(id)
        self.completed = False
        self.checkbox = Checkbox(value=False, label=name, data=self.id, onchange=self.checkbox_changed)
        self.textbox = Textbox(value=name, width='100%')
        self.stack_view = Stack(horizontal=True, horizontal_align='space-between',
                vertical_align='center', controls=[
                self.checkbox,
                Stack(horizontal=True, gap='0', controls=[
                    Button(icon='Edit', title='Edit todo', data=self.id, onclick=self.edit_clicked),
                    Button(icon='Delete', title='Delete todo', data=self.id, onclick=self.delete_clicked)]),
                ])
        
        #stack displayed when edit is clicked 
        self.stack_edit = Stack(visible=False, horizontal=True, horizontal_align='space-between',
                vertical_align='center', controls=[
                self.textbox, Button(text='Save', data=self.id, onclick=self.save_clicked)
                ])
        self.stack = Stack(controls=[self.stack_view, self.stack_edit])

    def edit_clicked(self, e):
        self.stack_view.visible = False
        self.stack_edit.visible = True
        self.app.update()

    def save_clicked(self, e):
        self.checkbox.label = self.textbox.value
        self.stack_view.visible = True
        self.stack_edit.visible = False
        self.app.update()

    def delete_clicked(self, e):
        self.app.delete_task(self)
        self.app.tasks_stack.controls.remove(self.stack)
        self.app.update()
    
    def checkbox_changed(self, e):
        if (self.checkbox.value and self.app.tabs.value=='active') or (self.checkbox.value==False and self.app.tabs.value=='completed'):
            self.stack.visible = False
        self.app.update()

class TodoApp():
    def __init__(self, page):
        self.tasks = []
        self.last_id = 0
        self.page = page
        self.new_task = Textbox(placeholder='Whats needs to be done?', width='100%')
        self.tasks_stack = Stack()
        self.items_left = Text('0 active items')
        self.tabs = Tabs(value='all', onchange=self.tabs_changed, tabs=[
                Tab(text='all'),
                Tab(text='active'),
                Tab(text='completed')])
        self.stack = Stack(width='70%', controls=[
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
        count = self.count_active_tasks()
        self.items_left.value = f"{count} active items left"
        self.page.update()

    def add_task(self, name):
        self.last_id += 1
        task = Task(self, self.last_id, name)
        self.tasks.append(task)
        return task

    def find_task(self, id):
        for task in self.tasks:
            if int(task.id) == int(id):
                return task

    def delete_task(self, task):
        self.tasks.remove(task)

    def count_active_tasks(self):
        result = 0
        for task in self.tasks:
            if task.checkbox.value == False:
                result += 1
        return result
    
    def add_clicked(self, e):
        task_name = self.new_task.value
        t = self.add_task(task_name)
        self.new_task.value = ''
        self.add_task_stack(t)
        self.update()       
    
    def clear_clicked(self, e):
        for task in self.tasks[:]:
            if task.checkbox.value == True:
                self.tasks_stack.controls.remove(task.stack)
                self.delete_task(task)
        self.update()

    def add_task_stack(self, task):
        self.tasks_stack.controls.append(task.stack)
        self.update()

    def tabs_changed(self, e):
        for task in self.tasks:
            if e.data=='all' or (e.data=='active' and task.checkbox.value==False) or (e.data=='completed' and task.checkbox.value):
                task.stack.visible = True
            else:
                task.stack.visible = False
        self.update()

def main(page):
    db = TodoApp(page)
    page.title = "Python Todo with Pglet"
    page.update()
    page.clean(True)
    page.add(db.stack)

#pglet.app("todo-app", target = main)
page = pglet.page("todo-app")
main(page)

input("Press Enter to exit...")