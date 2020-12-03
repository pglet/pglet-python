import pytest
import pglet
from pglet import Button

def test_button_primary_must_be_bool():
    with pytest.raises(Exception):
        Button(id="button1", text="My button", primary="1")

def test_button_add():
    b = Button(id="button1", text="My button")
    assert isinstance(b, pglet.Control)
    assert isinstance(b, pglet.Button)
    assert b.get_cmd_str() == ('button id="button1" text="My button"'), "Test failed"