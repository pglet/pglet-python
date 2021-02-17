import pglet
from pglet import Dialog, Text, Button

def test_dialog_add():
    d = Dialog(title='Hello', controls=[
        Text(value='Are you sure?')
        ], footer=[
        Button(text='OK'),
        Button(text="Cancel")
    ])

    assert isinstance(d, pglet.Control)
    assert isinstance(d, pglet.Dialog)
    assert d.get_cmd_str() == (
        'dialog title="Hello"\n'
        '  text value="Are you sure?"\n'
        '  footer\n'
        '    button text="OK"\n'
        '    button text="Cancel"'
    ), "Test failed"