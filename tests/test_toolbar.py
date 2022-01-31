import pglet
from pglet import Toolbar, toolbar


def test_toolbar_add():
    t = Toolbar(
        inverted=True,
        items=[
            toolbar.Item(
                text="text1",
                secondary_text="text2",
                url="url",
                new_window=True,
                icon="icon",
                icon_color="green",
                icon_only=False,
                split=True,
                divider=True,
            )
        ],
        overflow=[
            toolbar.Item(
                text="text12",
                secondary_text="text22",
                url="url2",
                new_window=True,
                icon="icon",
                icon_color="green",
                icon_only=False,
                split=True,
                divider=True,
            ),
            toolbar.Item(text="overflow"),
        ],
        far=[toolbar.Item(text="far")],
    )

    assert isinstance(t, pglet.Control)
    assert isinstance(t, pglet.Toolbar)
    assert t.get_cmd_str() == (
        'toolbar inverted="true"\n'
        '  item divider="true" icon="icon" iconcolor="green" icononly="false" newwindow="true" '
        'secondarytext="text2" split="true" text="text1" url="url"\n'
        "  overflow\n"
        '    item divider="true" icon="icon" iconcolor="green" icononly="false" newwindow="true" '
        'secondarytext="text22" split="true" text="text12" url="url2"\n'
        '    item text="overflow"\n'
        "  far\n"
        '    item text="far"'
    ), "Test failed"
