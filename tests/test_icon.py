import pglet
from pglet import Icon

def test_icon_add():
    c = Icon(name="Mail", color="#FF7F50", size="tiny")
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.Icon)
    #raise Exception(s.get_cmd_str())
    assert c.get_cmd_str() == ('icon color="#FF7F50" name="Mail" size="tiny"'), "Test failed"