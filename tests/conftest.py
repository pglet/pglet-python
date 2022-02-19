import pglet
import pytest
from pglet import Control
from pglet import Text


@pytest.fixture
def page():
    return pglet.page("test_update", no_window=True)


@pytest.fixture
def control_type_tree():
    def func(control: Control):
        if getattr(control, "controls", None):
            return {type(control): [func(child) for child in control.controls]}
        elif type(control) is Text:
            return control.value
        else:
            return type(control)

    return func