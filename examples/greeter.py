import pglet
from pglet import Textbox, Button, Text

def main(page):

    def btn_click(e):
        name = txt_name.value
        page.clean(True)
        page.add(Text(f"Hello, {name}!"))

    txt_name = Textbox("Your name")

    page.add(
        txt_name,
        Button("Say hello!", on_click=btn_click)
    )

pglet.app(target=main)