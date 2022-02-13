import pglet
from pglet.nav import Item
from pglet.protocol import Command


def test_item():
    ni = Item("key1")
    assert isinstance(ni, pglet.Control)
    assert isinstance(ni, Item)


def test_nav():
    n = pglet.Nav(
        id="list1",
        value="list1",
        items=[
            Item(
                key="key1",
                text="item1",
                icon="mail",
                icon_color="green",
                url="https://google.com",
                new_window=True,
                expanded=True,
            ),
            Item(key="key2", text="item2"),
        ],
    )

    assert isinstance(n, pglet.Control)
    assert isinstance(n, pglet.Nav)
    assert n.get_cmd_str() == [
        Command(
            indent=0, name=None, values=["nav"], attrs={"value": "list1", "id": ("list1", True)}, lines=[], commands=[]
        ),
        Command(
            indent=2,
            name=None,
            values=["item"],
            attrs={
                "expanded": "true",
                "icon": "mail",
                "iconcolor": "green",
                "key": "key1",
                "newwindow": "true",
                "text": "item1",
                "url": "https://google.com",
            },
            lines=[],
            commands=[],
        ),
        Command(indent=2, name=None, values=["item"], attrs={"key": "key2", "text": "item2"}, lines=[], commands=[]),
    ], "Test failed"

    ni = Item("key1")
    assert isinstance(ni, Item)


def test_nav_with_just_keys():
    n = pglet.Nav(id="list1", value="list1", items=[Item(key="key1"), Item(key="key2")])
    assert n.get_cmd_str() == [
        Command(
            indent=0, name=None, values=["nav"], attrs={"value": "list1", "id": ("list1", True)}, lines=[], commands=[]
        ),
        Command(indent=2, name=None, values=["item"], attrs={"key": "key1"}, lines=[], commands=[]),
        Command(indent=2, name=None, values=["item"], attrs={"key": "key2"}, lines=[], commands=[]),
    ], "Test failed"

    ni = Item("key1")
    assert isinstance(ni, Item)
