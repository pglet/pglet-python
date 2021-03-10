import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

# we are going to use pglet
import pglet

# from Pglet we need Page, Textbox, Button and Text controls
from pglet import Page, Textbox, Button, Text

# We define "main" function which is an entry point for our application and called for every new user session.
def main(page):

    # now we want the button to do something
    # we add a new event
    def on_click(e):
        # we get the entered text
        name = page.get_value(txt_name)

        # then cleaning the page
        page.clean()

        # and adding the text with our greeting
        page.add(Text(f"Hello, {name}!"))

    # on the page we need a textbox
    # and a button
    txt_name = Textbox("Your name")
    btn_hello = Button("Say hello!", onclick=on_click)

    # then we add controls to the page
    page.add(txt_name, btn_hello)

# then we wait for new users to connect
pglet.app(target=main, web=True)