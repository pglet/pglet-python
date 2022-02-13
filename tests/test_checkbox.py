import pglet
from pglet import Checkbox
from pglet.protocol import Command


def test_checkbox_add():
    c = Checkbox(label="Do you agree?", value=True, visible=True, box_side="start", data="data1")
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.Checkbox)
    assert c.get_cmd_str() == [
        Command(
            indent=0,
            name=None,
            values=["checkbox"],
            attrs={"boxside": "start", "data": "data1", "label": "Do you agree?", "value": "true", "visible": "true"},
            lines=[],
            commands=[],
        )
    ], "Test failed"
