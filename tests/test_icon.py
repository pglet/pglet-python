import pglet
from pglet import Icon
from pglet.protocol import Command


def test_icon_add():
    c = Icon(name="Mail", color="#FF7F50", size="tiny")
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.Icon)
    # raise Exception(s.get_cmd_str())
    assert c.get_cmd_str() == [
        Command(
            indent=0,
            name=None,
            values=["icon"],
            attrs={"color": "#FF7F50", "name": "Mail", "size": "tiny"},
            lines=[],
            commands=[],
        )
    ], "Test failed"
