import pglet
from pglet.protocol import Command


def test_textbox_add():
    tb = pglet.Textbox(id="txt1", label="Your name:")
    assert isinstance(tb, pglet.Control)
    assert isinstance(tb, pglet.Textbox)
    assert [
        Command(
            indent="  ",
            name=None,
            values=["textbox"],
            attrs={"label": "Your name:", "id": ("txt1", True)},
            lines=[],
            commands=[],
        )
    ], "Test failed"
