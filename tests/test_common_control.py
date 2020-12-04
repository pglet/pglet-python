import pytest
import pglet
from pglet import Text

@pytest.fixture
def page():
    return pglet.page("test_common_control", noWindow=True)

def test_show_hide(page):
    # open page
    page.add([
        Text(id="ctl1", value="Text1"),
        Text(id="ctl2", value="Text2"),
        Text(id="ctl3", value="Text3")
    ])
    page.hide("ctl1", "ctl2", "ctl3")

def test_remove_list(page):
    # open page
    #page.remove(at=0)

    page.add([
        Text(id="ctl1", value="Text1"),
        Text(id="ctl2", value="Text2"),
        Text(id="ctl3", value="Text3")
    ])
    page.remove("ctl1", "ctl2", "ctl3")

def test_remove_at(page):

    page.add(Text(id="ctl3", value="Text3"))

    page.remove(at=0)