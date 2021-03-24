import pglet
from pglet import Callout, Text, Button

def test_callout_add():
    c = Callout(target='button1', position='leftBottom', gap=100, beak=True, beak_width=10, page_padding=10,
    focus=False, cover=True, visible=True, controls=[
        Text(value='This is callout')
        ])

    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.Callout)
    assert c.get_cmd_str() == (
        'callout beak="true" beakWidth="10" cover="true" focus="false" gap="100" pagePadding="10" '
        'position="leftBottom" target="button1" visible="true"\n'
        '  text value="This is callout"'
    ), "Test failed"