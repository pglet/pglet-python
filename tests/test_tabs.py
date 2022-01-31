import pglet
from pglet import Button, Tab, Tabs, Textbox


def test_tabs_add():
    t = Tabs(tabs=[Tab(text="Tab1"), Tab("Tab2"), Tab("Tab3")])

    assert isinstance(t, pglet.Control)
    assert isinstance(t, pglet.Tabs)
    assert t.get_cmd_str() == (
        "tabs\n" '  tab text="Tab1"\n' '  tab text="Tab2"\n' '  tab text="Tab3"'
    ), "Test failed"


def test_tabs_with_controls_add():
    t = Tabs(
        tabs=[
            Tab(text="Tab1", controls=[Button(text="OK"), Button(text="Cancel")]),
            Tab(
                "Tab2",
                controls=[Textbox(label="Textbox 1"), Textbox(label="Textbox 2")],
            ),
        ]
    )
    assert isinstance(t, pglet.Control)
    assert isinstance(t, pglet.Tabs)
    assert t.get_cmd_str() == (
        "tabs\n"
        '  tab text="Tab1"\n'
        '    button text="OK"\n'
        '    button text="Cancel"\n'
        '  tab text="Tab2"\n'
        '    textbox label="Textbox 1"\n'
        '    textbox label="Textbox 2"'
    ), "Test failed"
