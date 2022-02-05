import pglet
from pglet import Text, Stack, Button

page = pglet.page("autoscroll", update=False, no_window=True, permissions="")
# page.theme_primary_color = "green"
# page.gap = 100
# page.padding = 100
# page.update()

st = Stack(scroll_y=True, auto_scroll=True)

scroll_box = Stack(
    height="400", width="100%", bgcolor="#f0f0f0", vertical_align="end", controls=[st]
)


def add_click(e):
    page.i += 1
    st.controls.append(Text(f"Line {page.i}"))
    st.update()


page.add(scroll_box, Button("Add line", primary=True, on_click=add_click))

for i in range(0, 10):
    st.controls.append(Text(f"Line {i}"))
    st.update()

page.i = i

input()
