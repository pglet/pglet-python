import pglet
from pglet import Link, Text

"""
def test_button_primary_must_be_bool():
    with pytest.raises(Exception):
        Button(id="button1", text="My button", primary="1")

"""


def test_link_add():
    l = Link(value="search", url="http://google.com", align="left", new_window=True)
    assert isinstance(l, pglet.Control)
    assert isinstance(l, pglet.Link)
    assert l.get_cmd_str() == (
        'link align="left" newwindow="true" url="http://google.com" value="search"'
    ), "Test failed"


def test_link_with_controls():
    l = Link(
        value="Visit google",
        url="https://google.com",
        pre=True,
        align="right",
        width="100",
        size="large1",
        title="Link title",
        controls=[Text(value="LinkText1"), Text(value="LinkText2")],
    )
    assert isinstance(l, pglet.Control)
    assert isinstance(l, pglet.Link)
    assert l.get_cmd_str() == (
        'link align="right" pre="true" size="large1" title="Link title" '
        'url="https://google.com" value="Visit google" width="100"\n'
        '  text value="LinkText1"\n'
        '  text value="LinkText2"'
    ), "Test failed"
