import pytest
import pglet
from pglet import Textbox, Stack

@pytest.fixture
def page():
    return pglet.page('test_add', noWindow=True)

def test_add_single_control(page):
    result = page.add(Textbox(id="txt1", label="First name:"))
    assert result == "txt1", "Test failed"

def test_add_controls_argv(page):
    result = page.add(
                Textbox(id="firstName", label="First name:"),
                Textbox(id="lastName", label="Last name:"),
                to="page", at=0)
    assert result == ["firstName", "lastName"], "Test failed"

def test_add_controls_list(page):
    result = page.add([
                Textbox(id="firstName", label="First name:"),
                Textbox(id="lastName", label="Last name:")],
                to="page", at=0)
    assert result == ["firstName", "lastName"], "Test failed"

def test_add_controls_to_another_control(page):
    stack = Stack(id="stack1", horizontal=True)
    page.add(stack)

    result = page.add(Textbox(id="firstName", label="First name:"),
                to=stack, at=0)

    assert result == "stack1:firstName", "Test failed"