import pglet
from pglet import Text, Stack, Button

def test_text_add():
    c = Text(value="Hello,\nworld!", markdown=True, align="left", vertical_align="top", size="tiny", bold=True, 
            italic=False, pre=False, nowrap=True, block=False, color='#9FE2BF', bgcolor='#FF7F50', 
            border='1px solid #550000', border_style='dotted', border_width='1', border_color='yellow', 
            border_radius='4px', border_left='1px solid #550000', border_right='1px solid #550000', 
            border_top='1px solid #550000', border_bottom='1px solid #550000')
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.Text)
    #raise Exception(s.get_cmd_str())
    #assert c.get_cmd_str() == ('text align="left" block="false" bold='true italic="false" nowrap="true" pre="false" size="tiny" value="Hello,\\nworld!" verticalAlign="left"'), "Test failed"
    assert c.get_cmd_str() == ('text align="left" bgcolor="#FF7F50" block="false" bold="true" '
    'border="1px solid #550000" borderBottom="1px solid #550000" borderColor="yellow" '
    'borderLeft="1px solid #550000" borderRadius="4px" borderRight="1px solid #550000" '
    'borderStyle="dotted" borderTop="1px solid #550000" borderWidth="1" color="#9FE2BF" '
    'italic="false" markdown="true" nowrap="true" pre="false" size="tiny" value="Hello,\\nworld!" '
    'verticalAlign="top"'), "Test failed"

def test_text_double_quotes():
    c = Text(value='Hello, "world!"')
    #raise Exception(c.get_cmd_str())
    assert c.get_cmd_str() == ('text value="Hello, \\"world!\\""'), "Test failed"

def test_add_text_inside_stack():
    txt = Text(id="txt1", value='Hello, "world!"')
    btn = Button(text="Super button")
    stack = Stack(id="header", controls=[txt, btn])

    # open page
    p = pglet.page('test_text', no_window=True)
    p.clean()

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