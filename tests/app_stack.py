import os

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text, Textbox, Slider, Message

def main(page):

    page.title = "Stack example"
    page.horizontal_align = 'stretch'
    page.update()

    bg_color = '#ddddee'

    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(Text(value=i, align='center', vertical_align='center', width=30, height=30, bgcolor='CyanBlue10', color='white', padding=5))
        return items

    def create_horizontal_stack(horiz_align):
        return Stack(controls=[
            Text(value=horiz_align),
            Stack(horizontal=True, horizontal_align=horiz_align, vertical_align='center', gap=20, bgcolor=bg_color, controls=items(3))
        ])

    def create_vertical_stack(vert_align):
        return Stack(width='20%', controls=[
            Text(value=vert_align),
            Stack(vertical_align=vert_align, horizontal_align='center', height=300, gap=20, bgcolor=bg_color, controls=items(3))
        ])
    
    # Gap, padding
    spacing_stack = Stack(horizontal=True, bgcolor=bg_color, gap=0, controls=items(5))
    
    def gap_slider_change(e):
        spacing_stack.gap = int(e.control.value)
        spacing_stack.update()
    gap_slider = Slider("Gap between items", min=0, max=50, step=1, value=0, show_value=True, on_change=gap_slider_change)

    def padding_slider_change(e):
        spacing_stack.padding = e.control.value
        spacing_stack.update()
    padding_slider = Slider("Stack padding", min=0, max=50, step=1, value=0, show_value=True, on_change=padding_slider_change)
    
    page.add(
        Text("Horizontal stack - Gap and Padding", size='xLarge'),
        gap_slider,
        padding_slider,
        spacing_stack
    )

    # Wrapping
    wrap_stack = Stack(horizontal=True, wrap=True, bgcolor=bg_color, gap=20, controls=items(10))
    def wrap_slider_change(e):
        width = int(e.control.value)
        wrap_stack.width = f"{width}%"
        wrap_stack.update()
    wrap_slider = Slider("Change the stack width to see how child items wrap onto multiple rows:",
        min=0, max=100, step=10, value=100, show_value=True, value_format='{value}%', on_change=wrap_slider_change)

    page.add(
        Text("Horizontal stack - Wrapping", size='xLarge'),
        wrap_slider,
        wrap_stack
    )

    # Horizontal stack
    page.add(
        Text("Horizontal stack - Horizontal Alignments", size='xLarge'),
        create_horizontal_stack('start'),
        create_horizontal_stack('center'),
        create_horizontal_stack('end'),
        create_horizontal_stack('space-between'),
        create_horizontal_stack('space-around'),
        create_horizontal_stack('space-evenly'),

        Text("Horizontal stack - Vertical Alignments", size='xLarge'),
        Text('start'),
        Stack(horizontal=True, vertical_align='start', height=100, bgcolor=bg_color, gap=20, controls=items(3)),
        Text('center'),
        Stack(horizontal=True, vertical_align='center', height=100, bgcolor=bg_color, gap=20, controls=items(3)),
        Text('end'),
        Stack(horizontal=True, vertical_align='end', height=100, bgcolor=bg_color, gap=20, controls=items(3))
    )

    # Vertical stack
    page.add(
        Text("Vertical stack - Vertical Alignments", size='xLarge'),
        Stack(horizontal=True, horizontal_align='space-between', width='100%', controls=[
            create_vertical_stack('start'),
            create_vertical_stack('center'),
            create_vertical_stack('end'),
            create_vertical_stack('space-between'),
            create_vertical_stack('space-around'),
            create_vertical_stack('space-evenly')
        ])
    )

    # Stack submit
    def stack_on_submit(e):
        stack = e.control
        stack.controls.insert(0, Message("Form has been submitted!", type='success', dismiss=True))
        stack.update()

    form1 = Stack(padding=10, width='50%', border='2px solid #eee', border_radius=5, controls=[
        Text("Pressing ENTER inside the stack will fire 'submit' event."),
        Textbox("First name"),
        Textbox("Last name")
    ], on_submit=stack_on_submit)

    page.add(
        Text("Stack with Submit event", size='xLarge'),
        form1
    )

pglet.app("python-stack", target=main)