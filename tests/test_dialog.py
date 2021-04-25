import pglet
from pglet import Dialog, Text, Button

def test_dialog_add():
    d = Dialog(open=True, title='Hello', sub_text='sub_text1',
    type='close', auto_dismiss=True, width=100,
    max_width=200, height=100, fixed_top=True, blocking=False, 
    data='data1', controls=[
        Text(value='Are you sure?')
        ], footer=[
        Button(text='OK'),
        Button(text="Cancel")
    ])

    assert isinstance(d, pglet.Control)
    assert isinstance(d, pglet.Dialog)
    assert d.get_cmd_str() == (
        'dialog autoDismiss="true" blocking="false" data="data1" fixedTop="true" '
        'height="100" maxWidth="200" open="true" subText="sub_text1" '
        'title="Hello" type="close" width="100"\n'
        '  text value="Are you sure?"\n'
        '  footer\n'
        '    button text="OK"\n'
        '    button text="Cancel"'
    ), "Test failed"