import os

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Checkbox, Button, Stack, Textbox, Tabs, Tab

class Task():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.completed = False

class Database():
    def __init__(self):
        self.tasks = []
        self.task_stacks = []
        self.last_id = 0

    def add_task(self, name):
        self.last_id += 1
        task = Task(self.last_id, name)
        self.tasks.append(task)
        return task

def main(page):
    db = Database()
    page.update(Page(title="Python Todo with Pglet"))
    page.clean()

    def add_clicked(e):
        task_name = page.get_value('new_task')
        t = db.add_task(task_name)
        add_task_stack(t)
        page.replace(db.task_stacks, to='tasks')
        page.set_value('new_task', '')
    
    def clear_clicked(e):
        db.task_stacks = []
        db.tasks = []
        page.replace(db.task_stacks, to='tasks')
        print('Clear completed button clicked!')

    def edit_clicked(e):
        print('Edit clicked!')

    def delete_clicked(e):
        print('Delete clicked!')

    def checkbox_clicked(e):
        print('Checkbox clicked!')

    
    def add_task_stack(task):
        s = Stack(id=str(task.id), horizontal=True, horizontal_align='space-between',
                vertical_align='center', controls=[
                Checkbox(id='status', value=task.completed, label=task.name, data='data'),
                Stack(horizontal=True, gap='0', controls=[
                    Button(id='edit', icon='Edit', title='Edit todo', data='data'),
                    Button(id='delete', icon='Delete', title='Delete todo', data='data')]),
                ])
        db.task_stacks.append(s)

    page.add(Stack(width='70%', controls=[
        Text(value='Todos', size='large', align='center'),
        Stack(horizontal=True, controls=[
            Textbox(id='new_task', placeholder='Whats needs to be done?', width='100%'),
            Button(id='add', primary=True, text='Add', onclick=add_clicked)]),
        Stack(gap=25, controls=[
            Tabs(tabs=[
                Tab(text='all'),
                Tab(text='active'),
                Tab(text='completed')]),
            Stack(id='tasks', controls=db.task_stacks),
            Stack(horizontal=True, horizontal_align='space-between', vertical_align='center', controls=[
                Text(id='items_left', value='0 items left'),
                Button(id='clear_completed', text='Clear completed', onclick=clear_clicked)
            ])
        ])
    ]))

    page.wait_close()    

pglet.app("todo-app", target = main)