import os

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text, Message, Button, Textbox, MessageButton

def messages():
  return Stack(width='70%', gap=20, controls=[
    Text("Messages", size="xLarge"),
    Message(value='This is just a message.'),
    Message(value='Success message with dismiss button', dismiss=True, type='success'),
    Message(value='Error message with dismiss button', dismiss=True, type='Error'),
    Message(type='blocked', truncated=True, dismiss=True, value='Blocked Message - single line, with dismiss button and truncated text. Truncation is not available if you use action buttons or multiline and should be used sparingly. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus, purus a lobortis tristique, odio augue pharetra metus, ac placerat nunc mi nec dui. Vestibulum aliquam et nunc semper scelerisque. Curabitur vitae orci nec quam condimentum porttitor et sed lacus. Vivamus ac efficitur leo. Cras faucibus mauris libero, ac placerat erat euismod et. Donec pulvinar commodo odio sit amet faucibus. In hac habitasse platea dictumst. Duis eu ante commodo, condimentum nibh pellentesque, laoreet enim. Fusce massa lorem, ultrices eu mi a, fermentum suscipit magna. Integer porta purus pulvinar, hendrerit felis eget, condimentum mauris. You\'ve been warned!'),
    Message(type='warning', dismiss=True, value='Warning message with buttons', buttons=[
        MessageButton(text='Yes', action='yes'),
        MessageButton(text='No', action='no')
    ]),
    Message(type='severeWarning', multiline=True, value='SevereWarning defaults to multiline. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus, purus a lobortis tristique, odio augue pharetra metus, ac placerat nunc mi nec dui. Vestibulum aliquam et nunc semper scelerisque. Curabitur vitae orci nec quam condimentum porttitor et sed lacus. Vivamus ac efficitur leo. Cras faucibus mauris libero, ac placerat erat euismod et. Donec pulvinar commodo odio sit amet faucibus. In hac habitasse platea dictumst. Duis eu ante commodo, condimentum nibh pellentesque, laoreet enim. Fusce massa lorem, ultrices eu mi a, fermentum suscipit magna. Integer porta purus pulvinar, hendrerit felis eget, condimentum mauris.', buttons=[
        MessageButton('OK'),
        MessageButton('Cancel')
    ]),
    message_with_on_dismiss(),
    message_with_on_dismiss_and_buttons(),
    Textbox(label="First name"),
    Textbox(label="Last name")
  ])

def message_with_on_dismiss():

  def message_dismissed(e):
    t.value = "Message dismissed!"
    stack.update()

  m = Message(value='Message with on_dismiss event', dismiss=True, on_dismiss=message_dismissed)
  t = Text()
  stack = Stack(controls=[m, t])
  return stack

def message_with_on_dismiss_and_buttons():

  def message_dismissed(e):
    t.value = f"Message dismissed with {e.data} action"
    stack.update()

  m = Message(value='Message with on_dismiss event and buttons', dismiss=True, on_dismiss=message_dismissed, buttons=[
      MessageButton('OK'),
      MessageButton('Cancel')
  ])
  t = Text()
  stack = Stack(controls=[m, t])
  return stack

def main(page):

    page.title = "Message control samples"
    page.horizontal_align = 'stretch'
    page.update()
    page.add(messages())

pglet.app("python-message", target = main, local=True)