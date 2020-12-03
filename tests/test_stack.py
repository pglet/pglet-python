import pglet
from pglet import Stack, Textbox, Button

def test_stack_add():
    s = Stack(controls=[
        Textbox(id="firstName"),
        Textbox(id="lastName")
    ])
    assert isinstance(s, pglet.Control)
    assert isinstance(s, pglet.Stack)
    #raise Exception(s.get_cmd_str())
    assert s.get_cmd_str() == (
        'stack\n'
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

def test_nested_stacks_update():
    stack = Stack(controls=[
        Textbox(id="firstName"),
        Textbox(id="lastName"),
        Stack(horizontal=True, controls=[
            Button(id="ok", text="OK"),
            Button(id="cancel", text="Cancel")
        ])
    ])

    # open page
    p = pglet.page(noWindow=True)
    ids = p.add(stack)

    assert ['_0', 'firstName', 'lastName', '_1', 'ok', 'cancel'] == ids, "Test failed"

    # raise Exception(stack.get_cmd_str(update=True))
    # assert stack.get_cmd_str(update=True) == (
    #     'stack\n'
    #     '  textbox id="firstName"\n'
    #     '  textbox id="lastName"\n'
    #     '  stack horizontal="true"\n'
    #     '    button id="ok" text="OK"\n'
    #     '    button id="cancel" text="Cancel"'
    # ), "Test failed"