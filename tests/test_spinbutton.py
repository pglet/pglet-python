import pglet
from pglet import SpinButton
from pglet.protocol import Command


def test_spinbutton_add():
    s = SpinButton(
        value=1,
        label="To what extent you agree",
        min=0,
        max=10,
        step=1,
        icon="icon_name",
        width=200,
        data="data1",
    )
    assert isinstance(s, pglet.Control)
    assert isinstance(s, pglet.SpinButton)
    assert s.get_cmd_str() == [
        Command(
            indent=0,
            name=None,
            values=["spinbutton"],
            attrs={
                "data": "data1",
                "icon": "icon_name",
                "label": "To what extent you agree",
                "max": "10",
                "min": "0",
                "step": "1",
                "value": "1",
                "width": "200",
            },
            lines=[],
            commands=[],
        )
    ], "Test failed"
