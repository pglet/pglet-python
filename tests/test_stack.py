import pglet
from pglet import Textbox

def test_textbox_add():
    tb = pglet.Textbox(id="txt1", label="Your name:")
    assert isinstance(tb, pglet.Control)
    assert isinstance(tb, pglet.Textbox)
    assert tb.get_cmd_str(indent='  ') == '  textbox id="txt1" label="Your name:"', "Test failed"

def test_textbox_update():
    tb = Textbox(id="txt1", errorMessage="Enter the value")
    assert tb.get_cmd_str(update=True) == 'id="txt1" errorMessage="Enter the value"', "Test failed"

def test_add_textbox():
    # open page
    p = pglet.page('test_textbox', noWindow=True)

    tb_value = "Line1\nLine2\nLine3"

    # add textbox
    tb_id = p.add(Textbox(value=tb_value, multiline=True))
    assert tb_id.startswith('_'), "Test failed"

    # get textbox value
    ret_tb_value = p.send(f"get {tb_id} value")
    assert ret_tb_value == tb_value, "Test failed"