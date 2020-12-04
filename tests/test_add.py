import pytest
import pglet
from pglet import Textbox, Stack

@pytest.fixture
def page():
    return pglet.page('test_add', no_window=True)

def test_add_single_control(page):
    result = page.add(Textbox(id="txt1", label="First name:"))
    assert result.id == "txt1", "Test failed"

def test_add_controls_argv(page):
    t1 = Textbox(id="firstName", label="First name:")
    t2 = Textbox(id="lastName", label="Last name:")
    result = page.add(t1, t2, to="page", at=0)
    assert result == [t1, t2], "Test failed"

def test_add_controls_list(page):
    t1 = Textbox(id="firstName", label="First name:")
    t2 = Textbox(id="lastName", label="Last name:")    
    result = page.add([t1, t2], to="page", at=0)
    assert result == [t1, t2], "Test failed"

def test_add_controls_to_another_control(page):
    stack = Stack(id="stack1", horizontal=True)
    page.add(stack)

    t1 = page.add(Textbox(id="firstName", label="First name:"),
                to=stack, at=0)

    assert t1.id == "stack1:firstName", "Test failed"