import pglet
from pglet import Checkbox


def test_checkbox_add():
    c = Checkbox(
        label="Do you agree?", value=True, visible=True, box_side="side1", data="data1"
    )
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.Checkbox)
    # raise Exception(s.get_cmd_str())
    assert c.get_cmd_str() == (
        'checkbox boxside="side1" data="data1" label="Do you agree?" '
        'value="true" visible="true"'
    ), "Test failed"
