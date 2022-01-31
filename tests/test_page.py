import pglet
from pglet import Page


def test_page():
    # create page
    p = pglet.page("test_page", local=True, no_window=True)

    assert p.url != "" and p.url.startswith("http"), "Test failed"
