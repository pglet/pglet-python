import pglet
from pglet import Message
from pglet.message import MessageButton

def test_button():
    b1 = MessageButton("text1")
    assert isinstance(b1, pglet.Control)
    assert isinstance(b1, MessageButton)

def test_message():
    m = pglet.Message(value='This is message', dismiss=True, buttons=[
    MessageButton(text='Yes, I agree', action='Yes'),
    MessageButton(text='No, I disagree', action='No')
])

    assert isinstance(m, pglet.Control)
    assert isinstance(m, pglet.Message)
    assert m.get_cmd_str() == (
        'message dismiss="true" value="This is message"\n'
        '  button action="Yes" text="Yes, I agree"\n'
        '  button action="No" text="No, I disagree"'
        ), "Test failed"

def test_message_button_with_just_text():
    m = pglet.Message(value='This is message', dismiss=True, buttons=[
        MessageButton(text='Yes, I agree'),
        MessageButton(text='No, I disagree')
        ])

    assert isinstance(m, pglet.Control)
    assert isinstance(m, pglet.Message)
    assert m.get_cmd_str() == (
        'message dismiss="true" value="This is message"\n'
        '  button text="Yes, I agree"\n'
        '  button text="No, I disagree"'
        ), "Test failed"

