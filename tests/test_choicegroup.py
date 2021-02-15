import pglet
from pglet import ChoiceGroup
from pglet.choicegroup import Option

def test_option():
    opt = Option("key1")
    assert isinstance(opt, pglet.Control)
    assert isinstance(opt, Option)

def test_choicegroup():
    cg = pglet.ChoiceGroup(id="list1", value='list1', label="Your favorite color:", options=[
        Option(key="key1", text="value1"),
        Option(key="key2", text="value2")]
        )

    assert isinstance(cg, pglet.Control)
    assert isinstance(cg, pglet.ChoiceGroup)
    assert cg.get_cmd_str() == (
        'dropdown id="list1" label="Your favorite color:"\n'
        '  option key="key1" text="value1"\n'
        '  option key="key2" text="value2"'
        ), "Test failed"

    cgo = Option("key1")
    assert isinstance(cgo, Option)

def test_choicegroup_with_just_keys():
    cg = pglet.ChoiceGroup(id="list1", label="Your favorite color:")
    cg.add_option("key1")
    cg.add_option("key2")
    assert cg.get_cmd_str(indent='  ') == (
        '  dropdown id="list1" label="Your favorite color:"\n'
        '    option key="key1"\n'
        '    option key="key2"'
        ), "Test failed"

    cgo = Option("key1")
    assert isinstance(cgo, Option)
