import pglet
from pglet import Panel, Text, Button

def test_panel_add():
    p = Panel(open=True, title='Hello', type='small',
    auto_dismiss=True, light_dismiss=False, width=100,
    blocking=False, data='data1', controls=[
        Text(value='Are you sure?')
        ], footer=[
        Button(text='OK'),
        Button(text="Cancel")
    ])

    assert isinstance(p, pglet.Control)
    assert isinstance(p, pglet.Panel)
    assert p.get_cmd_str() == (
        'panel Width="100" autoDismiss="true" blocking="false" data="data1" lightDismiss="false" '
        'open="true" title="Hello" type="small"\n'
        '  text value="Are you sure?"\n'
        '  footer\n'
        '    button text="OK"\n'
        '    button text="Cancel"'
    ), "Test failed"