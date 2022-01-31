import pglet
from pglet import Textbox


def test_textbox_add():
    tb = pglet.Textbox(id="txt1", label="Your name:")
    assert isinstance(tb, pglet.Control)
    assert isinstance(tb, pglet.Textbox)
    assert (
        tb.get_cmd_str(indent="  ") == '  textbox id="txt1" label="Your name:"'
    ), "Test failed"
