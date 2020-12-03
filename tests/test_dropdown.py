import pglet
from pglet import Dropdown
from pglet.dropdown import Option

def test_dropdown():
    dd = pglet.Dropdown(id="list1", label="Your favorite color:", options=[
        ("key1", "value1"),
        ("key2", "value2")
    ])

    assert isinstance(dd, pglet.Control)
    assert isinstance(dd, pglet.Dropdown)
    assert dd.get_cmd_str() == (
        'dropdown id="list1" label="Your favorite color:"\n'
        '  option key="key1" text="value1"\n'
        '  option key="key2" text="value2"'
        ), "Test failed"

    do = Option("key1")
    assert isinstance(do, Option)

def test_dropdown_with_just_keys():
    dd = pglet.Dropdown(id="list1", label="Your favorite color:")
    dd.add_option("key1")
    dd.add_option("key2")
    assert dd.get_cmd_str(indent='  ') == (
        '  dropdown id="list1" label="Your favorite color:"\n'
        '    option key="key1"\n'
        '    option key="key2"'
        ), "Test failed"

    do = Option("key1")
    assert isinstance(do, Option)

def test_dropdown_update():
    dd = pglet.Dropdown(id="list1", label="Your favorite color:", options=[
        Option("key1"),
        Option("key2")
    ])

    assert dd.get_cmd_str(update=True) == 'id="list1" label="Your favorite color:"', "Test failed"