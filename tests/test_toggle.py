import pytest
import pglet
from pglet import Toggle

'''
def test_button_primary_must_be_bool():
    with pytest.raises(Exception):
        Button(id="button1", text="My button", primary="1")

'''

def test_toggle_add():
    t = Toggle(value=True, label="This is toggle", inline=True, on_text='on text', off_text='off text')
    assert isinstance(t, pglet.Control)
    assert isinstance(t, pglet.Toggle)
    assert t.get_cmd_str() == ('toggle inline="true" label="This is toggle" offText="off text" onText="on text" value="true"'), "Test failed"