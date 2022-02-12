import pglet
from pglet import Stack, Text

page = pglet.page("text")
page.add(
    Stack(
        horizontal=True,
        controls=[
            Text(
                "This-is-a-very-long-text",
                width=50,
                height=50,
                border_style="double",
                border_width=1,
                # vertical_align="center",
                block=True,
                nowrap=True,
            ),
            Text(
                "This-is-a-very-long-text",
                width=50,
                height=50,
                border_style="double",
                border_width=1,
                vertical_align="center",
                block=True,
                nowrap=True,
            ),
        ],
    )
)
