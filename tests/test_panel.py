import pglet
from pglet import Button, Panel, Text


def test_panel_add():
    p = Panel(
        open=True,
        title="Hello",
        type="small",
        auto_dismiss=True,
        light_dismiss=False,
        width=100,
        blocking=False,
        data="data1",
        controls=[Text(value="Are you sure?")],
        footer=[Button(text="OK"), Button(text="Cancel")],
    )

    assert isinstance(p, pglet.Control)
    assert isinstance(p, pglet.Panel)
    assert p.get_cmd_str() == (
        'panel autodismiss="true" blocking="false" data="data1" lightdismiss="false" '
        'open="true" title="Hello" type="small" width="100"\n'
        '  text value="Are you sure?"\n'
        "  footer\n"
        '    button text="OK"\n'
        '    button text="Cancel"'
    ), "Test failed"
