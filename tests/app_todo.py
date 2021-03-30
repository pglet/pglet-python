import os

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Checkbox, Button, Stack, Textbox, Tabs, Tab

class Task():
    def __init__(self, id, name, on_status_change, on_edit_clicked, on_save_clicked, on_delete_clicked):
        self.id = str(id)
        self.completed = False
        self.checkbox = Checkbox(value=False, label=name, data=self.id, onchange=on_status_change)
        self.textbox = Textbox(value=name, width='100%')
        self.stack_view = Stack(horizontal=True, horizontal_align='space-between',
                vertical_align='center', controls=[
                self.checkbox,
                Stack(horizontal=True, gap='0', controls=[
                    Button(icon='Edit', title='Edit todo', data=self.id, onclick=on_edit_clicked),
                    Button(icon='Delete', title='Delete todo', data=self.id, onclick=on_delete_clicked)]),
                ])
        
        #stack displayed when edit is clicked 
        self.stack_edit = Stack(visible=False, horizontal=True, horizontal_align='space-between',
                vertical_align='center', controls=[
                self.textbox, Button(text='Save', data=self.id, onclick=on_save_clicked)
                ])
        self.stack = Stack(controls=[self.stack_view, self.stack_edit])

class Database():
    def __init__(self):
        self.tasks = []
        self.last_id = 0
        self.items_left = 0

    def add_task(self, name, on_status_change, on_edit_clicked, on_save_clicked, on_delete_clicked):
        self.last_id += 1
        task = Task(self.last_id, name, on_status_change, on_edit_clicked, on_save_clicked, on_delete_clicked)
        self.tasks.append(task)
        self.items_left+=1
        return task

    def find_task(self, id):
        for task in self.tasks:
            if int(task.id) == int(id):
                return task

    def delete_task(self, task):
        self.tasks.remove(task)
        self.items_left-=1


def main(page):
    db = Database()
    page.title = "Python Todo with Pglet"
    page.update()
    page.clean(True)

    def add_clicked(e):
        task_name = new_task.value
        t = db.add_task(task_name, checkbox_changed, edit_clicked, save_clicked, delete_clicked)
        new_task.value = ''
        add_task_stack(t)
        
    
    def clear_clicked(e):
        for task in db.tasks[:]:
            print(task.checkbox.value)
            if task.checkbox.value == True:
                tasks_stack.controls.remove(task.stack)
                db.delete_task(task)
        items_left.value=str(db.items_left) +' items left'
        page.update()

    def edit_clicked(e):
        id = e.control.data
        task = db.find_task(id)
        task.stack_view.visible = False
        task.stack_edit.visible = True
        print(task.checkbox.value)
        page.update()

    def save_clicked(e):
        id = e.control.data
        task = db.find_task(id)
        task.checkbox.label = task.textbox.value
        task.stack_view.visible = True
        task.stack_edit.visible = False
        page.update()


    def delete_clicked(e):
        id = e.control.data
        task = db.find_task(id)
        db.delete_task(task)
        tasks_stack.controls.remove(task.stack)
        items_left.value=str(db.items_left) +' items left'
        page.update()

    def checkbox_changed(e):
        id = e.control.data
        task = db.find_task(id)

        if task.checkbox.value == True:
            db.items_left-=1
            if tabs.value == 'active':
                tasks_stack.controls.remove(task.stack)
        else:
            db.items_left+=1
            if tabs.value == 'completed':
                tasks_stack.controls.remove(task.stack)

        items_left.value=str(db.items_left) +' items left'
        page.update()

    def add_task_stack(task):
        tasks_stack.controls.append(task.stack)
        items_left.value=str(db.items_left) +' items left'
        page.update()

    def tabs_changed(e):
        tasks_stack.controls.clear()
        if e.data == 'all':
            for task in db.tasks:
                tasks_stack.controls.append(task.stack)
        elif e.data == 'active':
            for task in db.tasks:
                if task.checkbox.value == False:
                    tasks_stack.controls.append(task.stack)
        elif e.data == 'completed':
             for task in db.tasks:
                if task.checkbox.value == True:
                    tasks_stack.controls.append(task.stack)
        page.update()
    
    new_task = Textbox(placeholder='Whats needs to be done?', width='100%')
    tasks_stack = Stack()

    items_left = Text(value='0 items left')
    tabs = Tabs(value='all', onchange=tabs_changed, tabs=[
                Tab(text='all'),
                Tab(text='active'),
                Tab(text='completed')])

    page.add(Stack(width='70%', controls=[
        Text(value='Todos', size='large', align='center'),
        Stack(horizontal=True, controls=[
            new_task,
            Button(id='add', primary=True, text='Add', onclick=add_clicked)]),
        Stack(gap=25, controls=[
            tabs,
            tasks_stack,
            Stack(horizontal=True, horizontal_align='space-between', vertical_align='center', controls=[
                items_left,
                Button(id='clear_completed', text='Clear completed', onclick=clear_clicked)
            ])
        ])
    ])) 

#pglet.app("todo-app", target = main)
page = pglet.page("todo-app")
main(page)

input("Press Enter to exit...")