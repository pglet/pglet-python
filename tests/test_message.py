import pglet
from pglet.message import MessageButton
from pglet.protocol import Command


def test_button():
    b1 = MessageButton("text1")
    assert isinstance(b1, pglet.Control)
    assert isinstance(b1, MessageButton)


def test_message():
    m = pglet.Message(
        value="This is message",
        dismiss=True,
        buttons=[
            MessageButton(text="Yes, I agree", action="Yes"),
            MessageButton(text="No, I disagree", action="No"),
        ],
    )

    assert isinstance(m, pglet.Control)
    assert isinstance(m, pglet.Message)
    assert m.get_cmd_str() == [
        Command(
            indent=0,
            name=None,
            values=["message"],
            attrs={"dismiss": "true", "value": "This is message"},
            lines=[],
            commands=[],
        ),
        Command(
            indent=2,
            name=None,
            values=["button"],
            attrs={"action": "Yes", "text": "Yes, I agree"},
            lines=[],
            commands=[],
        ),
        Command(
            indent=2,
            name=None,
            values=["button"],
            attrs={"action": "No", "text": "No, I disagree"},
            lines=[],
            commands=[],
        ),
    ], "Test failed"


def test_message_button_with_just_text():
    m = pglet.Message(
        value="This is message",
        dismiss=True,
        buttons=[
            MessageButton(text="Yes, I agree"),
            MessageButton(text="No, I disagree"),
        ],
    )

    assert isinstance(m, pglet.Control)
    assert isinstance(m, pglet.Message)
    assert m.get_cmd_str() == [
        Command(
            indent=0,
            name=None,
            values=["message"],
            attrs={"dismiss": "true", "value": "This is message"},
            lines=[],
            commands=[],
        ),
        Command(indent=2, name=None, values=["button"], attrs={"text": "Yes, I agree"}, lines=[], commands=[]),
        Command(indent=2, name=None, values=["button"], attrs={"text": "No, I disagree"}, lines=[], commands=[]),
    ], "Test failed"
