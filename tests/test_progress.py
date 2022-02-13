import pglet
from pglet import Progress
from pglet.protocol import Command


def test_progress_add():
    c = Progress(label="Doing something...", value=10)
    assert isinstance(c, pglet.Control)
    assert isinstance(c, pglet.Progress)
    # raise Exception(s.get_cmd_str())
    assert c.get_cmd_str() == [
        Command(
            indent=0,
            name=None,
            values=["progress"],
            attrs={"label": "Doing something...", "value": "10"},
            lines=[],
            commands=[],
        )
    ], "Test failed"
