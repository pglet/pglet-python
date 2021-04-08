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
        self.display_task = Checkbox(value=False, label=name, onchange=self.status_changed)
        self.edit_name = Textbox(width='100%')
        self.display_view = Stack(horizontal=True, horizontal_align='space-between',
                vertical_align='center', controls=[
                self.display_task,
                Stack(horizontal=True, gap='0', controls=[
                    Button(icon='Edit', title='Edit todo', onclick=self.edit_clicked),
                    Button(icon='Delete', title='Delete todo', onclick=self.delete_clicked)]),
                ])
        
        #stack displayed when edit is clicked 
        self.edit_view = Stack(visible=False, horizontal=True, horizontal_align='space-between',
                vertical_align='center', controls=[
                self.edit_name, Button(text='Save', onclick=self.save_clicked)
                ])
        self.view = Stack(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.app.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.app.update()

    def delete_clicked(self, e):
        self.app.delete_task(self)
    
    def status_changed(self, e):
        self.app.update()

class TodoApp():
    def __init__(self):
        self.tasks = []
        self.new_task = Textbox(placeholder='Whats needs to be done?', width='100%')
        self.tasks_view = Stack()
        self.items_left = Text('0 active items')
        self.filter = Tabs(value='all', onchange=self.tabs_changed, tabs=[
                Tab(text='all'),
                Tab(text='active'),
                Tab(text='completed')])
        self.view = Stack(width='70%', controls=[
            Text(value='Todos', size='large', align='center'),
            Stack(horizontal=True, controls=[
                self.new_task,
                Button(primary=True, text='Add', onclick=self.add_clicked)]),
            Stack(gap=25, controls=[
                self.filter,
                self.tasks_view,
                Stack(horizontal=True, horizontal_align='space-between', vertical_align='center', controls=[
                    self.items_left,
                    Button(text='Clear completed', onclick=self.clear_clicked)
                ])
            ])
        ])

    def update(self):
        count = 0
        status = self.filter.value
        for task in self.tasks:
            task.view.visible = status == 'all' or (status == 'active' and task.display_task.value == False) or (status == 'completed' and task.display_task.value)
            if task.display_task.value == False:
                count += 1
        self.items_left.value = f"{count} active items left"
        self.view.update()

    def delete_task(self, task):
        self.tasks.remove(task)
        self.tasks_view.controls.remove(task.view)
        self.update()
    
    def add_clicked(self, e):
        task = Task(self, self.new_task.value)
        self.tasks.append(task)
        self.tasks_view.controls.append(task.view)
        self.new_task.value = ''
        self.update()
    
    def clear_clicked(self, e):
        for task in self.tasks[:]:
            if task.display_task.value == True:
                self.delete_task(task)

    def tabs_changed(self, e):
        self.update()

def main(page):

    print("Initial hash:", page.hash)

    page.title = "Python Todo with Pglet"
    page.update()
    page.clean(True)

    def on_close(e):
        print("session closed")

    def on_hash_change(e):
        print("hash changed:", e.data)

    page.onclose = on_close
    page.onhashchange = on_hash_change

    app1 = TodoApp()
    page.add(app1.view)

    app2 = TodoApp()
    page.add(app2.view)

pglet.app("todo-app", target = main)
#page = pglet.page("todo-app", no_window=True)
#main(page)

input("Press Enter to exit...")