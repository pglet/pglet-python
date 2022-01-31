import pglet
from pglet import Button, Stack, Text


def test_text_add():
    c = Text(
        value="Hello,\nworld!",
        markdown=True,
        align="left",
        vertical_align="top",
        size="tiny",
        bold=True,
        italic=False,
        pre=False,
        nowrap=True,
        block=False,
        color="#9FE2BF",
        bgcolor="#FF7F50",
        border="1px solid #550000",
        border_style="dotted",
        border_width="1",
        border_color="yellow",
        border_radius="4px",
        border_left="1px solid #550000",
        border_right="1px solid #550000",
        border_top="1px solid #550000",
        border_bottom="1px solid #550000",
    )
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.Text)
    # raise Exception(s.get_cmd_str())
    # assert c.get_cmd_str() == ('text align="left" block="false" bold='true italic="false" nowrap="true" pre="false" size="tiny" value="Hello,\\nworld!" verticalAlign="left"'), "Test failed"
    assert c.get_cmd_str() == (
        'text align="left" bgcolor="#FF7F50" block="false" bold="true" '
        'border="1px solid #550000" borderbottom="1px solid #550000" bordercolor="yellow" '
        'borderleft="1px solid #550000" borderradius="4px" borderright="1px solid #550000" '
        'borderstyle="dotted" bordertop="1px solid #550000" borderwidth="1" color="#9FE2BF" '
        'italic="false" markdown="true" nowrap="true" pre="false" size="tiny" value="Hello,\\nworld!" '
        'verticalalign="top"'
    ), "Test failed"


def test_text_double_quotes():
    c = Text(value='Hello, "world!"')
    # raise Exception(c.get_cmd_str())
    assert c.get_cmd_str() == ('text value="Hello, \\"world!\\""'), "Test failed"


def test_add_text_inside_stack():
    txt = Text(id="txt1", value='Hello, "world!"')
    btn = Button(text="Super button")
    stack = Stack(id="header", controls=[txt, btn])

    # open page
    p = pglet.page("test_text", local=True, no_window=True)
    p.clean()
