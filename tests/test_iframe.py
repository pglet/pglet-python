from typing import List

import pglet
from pglet import IFrame
from pglet.protocol import Command


def test_iframe_add():
    c = IFrame(src="https://google.com", border_style="solid")
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.IFrame)

    assert c.get_cmd_str() == [
        Command(
            indent=0,
            name=None,
            values=["iframe"],
            attrs={"borderstyle": "solid", "src": "https://google.com"},
            lines=[],
            commands=[],
        )
    ], "Test failed"


def test_iframe_multiple_border_styles():
    c = IFrame(src="https://google.com", border_style=["solid", "none", "groove"])
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.IFrame)

    # check property reading
    style = c.border_style
    assert isinstance(style, List)
    assert len(style) == 3

    assert c.get_cmd_str() == [
        Command(
            indent=0,
            name=None,
            values=["iframe"],
            attrs={"borderstyle": "solid none groove", "src": "https://google.com"},
            lines=[],
            commands=[],
        )
    ], "Test failed"
