import pglet
from pglet import Text, Stack, Button

page = pglet.page("autoscroll", update=False, permissions="")
# page.theme = "dark"
# page.gap = 100
# page.padding = 100
# page.update()

st = Stack(
    height="400", width="100%", bgcolor="#f0f0f0", scroll_y=True, auto_scroll=True
)


def add_click(e):
    page.i += 1
    st.controls.append(Text(f"Line {page.i}"))
    st.update()


page.add(st, Button("Add line", on_click=add_click))

for i in range(0, 50):
    st.controls.append(Text(f"Line {i}"))
    st.update()

page.i = i

input()
