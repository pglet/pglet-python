import pytest
import pglet
from pglet import Textbox


@pytest.fixture
def page():
    return pglet.page("test_update", local=True, no_window=True)


def test_update_single_control(page):
    txt = Textbox(id="txt1", label="First name:")
    page.add(txt)
    page.update(txt)
