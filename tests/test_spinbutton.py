import pglet
from pglet import SpinButton


def test_searchbox_add():
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
    assert s.get_cmd_str() == (
        'spinbutton data="data1" icon="icon_name" '
        'label="To what extent you agree" max="10" min="0" step="1" value="1" width="200"'
    ), "Test failed"
