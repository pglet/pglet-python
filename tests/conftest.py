import pglet
import pytest


@pytest.fixture
def page():
    return pglet.page("test_update", no_window=True)
