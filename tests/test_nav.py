import pglet
from pglet import Nav
from pglet.nav import Item

def test_item():
    ni = Item("key1")
    assert isinstance(ni, pglet.Control)
    assert isinstance(ni, Item)

def test_nav():
    n = pglet.Nav(id="list1", value="list1", items=[
        Item(key="key1", text="item1"),
        Item(key="key2", text="item2")
    ])

    assert isinstance(n, pglet.Control)
    assert isinstance(n, pglet.Nav)
    assert n.get_cmd_str() == (
        'nav id="list1" value="list1"\n'
        '  item key="key1" text="item1"\n'
        '  item key="key2" text="item2"'
        ), "Test failed"

    ni = Item("key1")
    assert isinstance(ni, Item)

def test_nav_with_just_keys():
    n = pglet.Nav(id="list1", value="list1")
    n.add_item("key1")
    n.add_item("key2")
    assert n.get_cmd_str(indent='  ') == (
        '  nav id="list1" value="list1"\n'
        '    item key="key1"\n'
        '    item key="key2"'
        ), "Test failed"

    ni = Item("key1")
    assert isinstance(ni, Item)

def test_nav_update():
    n = pglet.Nav(id="list1", value="list1", items=[
        Item("key1"),
        Item("key2")
    ])

    p = pglet.page(no_window=True)
    p.add(n)

    assert n.get_cmd_str(update=True) == '', "Test failed"

    n.items[0].key = 1
    n.items[1].text = "Key 2"

    assert n.get_cmd_str(update=True) == (
        '"list1:_1" key="1"\n'
        '"list1:_2" text="Key 2"'
    ), "Test failed"