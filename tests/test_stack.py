import pglet
from pglet import Stack, Textbox, Button

def test_stack_add():
    s = Stack(horizontal=True, vertical_fill=True, horizontal_align='center', vertical_align='baseline',
    gap='large', wrap=True, scrollx=True, scrolly=True, controls=[
        Textbox(id="firstName"),
        Textbox(id="lastName")
    ])
    assert isinstance(s, pglet.Control)
    assert isinstance(s, pglet.Stack)
    #raise Exception(s.get_cmd_str())
    assert s.get_cmd_str() == (
        'stack gap="large" horizontal="true" horizontalalign="center" '
        'scrollx="true" scrolly="true" verticalalign="baseline" verticalfill="true" wrap="true"\n'
        '  textbox id="firstName"\n'
        '  textbox id="lastName"'
    ), "Test failed"

def test_nested_stacks_add():
    s = Stack(controls=[
        Textbox(id="firstName"),
        Textbox(id="lastName"),
        Stack(horizontal=True, controls=[
            Button(id="ok", text="OK", primary=True),
            Button(id="cancel", text="Cancel")
        ])
    ])
    assert isinstance(s, pglet.Control)
    assert isinstance(s, pglet.Stack)
    #raise Exception(s.get_cmd_str())
    assert s.get_cmd_str() == (
        'stack\n'
        '  textbox id="firstName"\n'
        '  textbox id="lastName"\n'
        '  stack horizontal="true"\n'
        '    button id="ok" primary="true" text="OK"\n'
        '    button id="cancel" text="Cancel"'
    ), "Test failed"