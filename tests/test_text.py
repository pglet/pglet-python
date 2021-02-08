import pglet
from pglet import Text, Stack, Button

def test_text_add():
    c = Text(value="Hello,\nworld!", align="left", verticalAlign="left", size="tiny", bold=True, italic=False, 
            pre=False, nowrap=True, block=False, color='#9FE2BF', bgcolor='#FF7F50', border='1px solid #550000')
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.Text)
    #raise Exception(s.get_cmd_str())
    #assert c.get_cmd_str() == ('text align="left" block="false" bold="true" italic="false" nowrap="true" pre="false" size="tiny" value="Hello,\\nworld!" verticalAlign="left"'), "Test failed"
    assert c.get_cmd_str() == ('text align="left" bgcolor="#FF7F50" '
        'block="false" bold="true" border="1px solid #550000" color="#9FE2BF" '
        'italic="false" nowrap="true" '
        'pre="false" size="tiny" value="Hello,\\nworld!" '
        'verticalAlign="left"'), "Test failed"

def test_text_double_quotes():
    c = Text(value='Hello, "world!"')
    #raise Exception(c.get_cmd_str())
    assert c.get_cmd_str() == ('text value="Hello, \\"world!\\""'), "Test failed"

def test_add_text_inside_stack():
    txt = Text(id="txt1", value="Hello,\nworld!")
    btn = Button(text="Super button")
    stack = Stack(id="header", controls=[txt, btn])

    # open page
    p = pglet.page('test_text', no_window=True)

    # add control first time
    p.add(stack)
    btnId = btn.id
    assert btnId.startswith("header:_"), "Test failed"
    assert txt.id == "header:txt1", "Test failed"
    assert stack.id == "header", "Test failed"

    # add control second time
    p.add(stack)
    assert btn.id.startswith("header:_") and btn.id != btnId, "Test failed"
    assert txt.id == "header:txt1", "Test failed"
    assert stack.id == "header", "Test failed"