import pglet
from pglet import Dropdown

def test_dropdown():
    dd = pglet.Dropdown(id="list1", label="Your favorite color:", options=[
        ("key1", "value1"),
        ("key2", "value2")
    ])
    assert isinstance(dd, pglet.Control)
    assert isinstance(dd, pglet.Dropdown)
    assert dd.add_cmd() == "dropdown id=\"list1\" label=\"Your favorite color:\"", "Test failed"

    do = Dropdown.Option()
    assert isinstance(do, Dropdown.Option)