import pglet
from pglet import Checkbox

def test_checkbox_add():
    c = Checkbox(label="Do you agree?", value=True, visible=True)
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.Checkbox)
    #raise Exception(s.get_cmd_str())
    assert c.get_cmd_str() == ('checkbox visible="true" label="Do you agree?" value="true"'), "Test failed"