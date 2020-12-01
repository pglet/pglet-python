import pytest
import pglet
from pglet import Textbox

@pytest.fixture
def page():
    return pglet.page('page1', noWindow=True)

def test_update_should_fail_without_id(page):
    with pytest.raises(Exception):
        page.update(Textbox(label="First name:"))

def test_update_single_control(page):
    page.update(Textbox(id="txt1", label="First name:"))