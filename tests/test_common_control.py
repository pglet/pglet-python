import pytest
import pglet

@pytest.fixture
def page():
    return pglet.page('page1', noWindow=True)

def test_show_hide(page):
    # open page
    page.hide("ctl1", "ctl2", "ctl3")

def test_remove_at(page):
    # open page
    page.remove(at=0)
    page.remove("ctl1", "ctl2", "ctl3")