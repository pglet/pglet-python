import pytest
import pglet
from pglet import Link

'''
def test_button_primary_must_be_bool():
    with pytest.raises(Exception):
        Button(id="button1", text="My button", primary="1")

'''

def test_link_add():
    l = Link(value="search", url="http://google.com", align="left", new_window=True)
    assert isinstance(l, pglet.Control)
    assert isinstance(l, pglet.Link)
    assert l.get_cmd_str() == ('link align="left" newWindow="true" url="http://google.com" value="search"'), "Test failed"