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
    ctrls = p.add(stack)

    assert ['_0', 'firstName', 'lastName', '_1', 'ok', 'cancel'] == [ctrls[0].id, ctrls[1].id, ctrls[2].id, ctrls[3].id, ctrls[4].id, ctrls[5].id], "Test failed"

    # empty update
    assert stack.get_cmd_str(update=True) == "", "Test failed"

    # update stack element
    ctrls[0].horizontal=True
    assert stack.get_cmd_str(update=True) == '"_0" horizontal="true"', "Test failed"

    # update inner elements
    ctrls[1].value = "John"
    ctrls[2].value = "Smith"
    ctrls[4].primary = True

    #raise Exception(stack.get_cmd_str(update=True))

    assert stack.get_cmd_str(update=True) == (
        '"firstName" value="John"\n'
        '"lastName" value="Smith"\n'
        '"ok" primary="true"'
    ), "Test failed"    

    

    # assert stack.get_cmd_str(update=True) == (
    #     'stack\n'
    #     '  textbox id="firstName"\n'
    #     '  textbox id="lastName"\n'
    #     '  stack horizontal="true"\n'
    #     '    button id="ok" text="OK"\n'
    #     '    button id="cancel" text="Cancel"'
    # ), "Test failed"