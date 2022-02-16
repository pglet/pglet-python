import logging

import pglet
from pglet import SplitStack, Stack, Text
from pglet.button import Button

logging.basicConfig(level=logging.DEBUG)

page = pglet.page("split1")
page.title = "Split test"
page.horizontal_align = "stretch"
page.vertical_fill = True
st = SplitStack(
    height="100%",
    horizontal=True,
    # gutter_color="#eee",
    gutter_size=10,
    controls=[
        Stack(width="200", min_width="200", height="100%", controls=[Text("Column A")]),
        Stack(height="100%", controls=[Text("Column B")]),
        Stack(
            height="100%",
            width="30%",
            controls=[
                SplitStack(
                    height="100%",
                    gutter_color="yellow",
                    gutter_hover_color="orange",
                    gutter_drag_color="blue",
                    controls=[
                        Stack(
                            width="100%",
                            bgcolor="lightGreen",
                            controls=[Text("Row A")],
                        ),
                        Stack(
                            width="100%",
                            height="200",
                            max_height="400",
                            bgcolor="lightGreen",
                            controls=[Text("Row B")],
                        ),
                    ],
                )
            ],
        ),
    ],
)


def btn_click(e):
    st.height = "90%"
    st.update()


btn = Button("Click me!", on_click=btn_click)
page.add(btn, st)

input()
