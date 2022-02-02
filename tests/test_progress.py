import pglet
from pglet import Progress


def test_progress_add():
    c = Progress(label="Doing something...", value=10)
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.Progress)
    # raise Exception(s.get_cmd_str())
    assert c.get_cmd_str() == (
        'progress label="Doing something..." value="10"'
    ), "Test failed"
