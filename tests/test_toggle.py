import pglet
from pglet import Toggle
from pglet.protocol import Command

"""
def test_button_primary_must_be_bool():
    with pytest.raises(Exception):
        Button(id="button1", text="My button", primary="1")

"""


def test_toggle_add():
    t = Toggle(
        value=True,
        label="This is toggle",
        inline=True,
        on_text="on text",
        off_text="off text",
    )
    assert isinstance(t, pglet.Control)
    assert isinstance(t, pglet.Toggle)
    assert t.get_cmd_str() == [
        Command(
            indent=0,
            name=None,
            values=["toggle"],
            attrs={
                "inline": "true",
                "label": "This is toggle",
                "offtext": "off text",
                "ontext": "on text",
                "value": "true",
            },
            lines=[],
            commands=[],
        )
    ], "Test failed"
