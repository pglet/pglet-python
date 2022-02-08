import pglet
from pglet import ComboBox, combobox

page = pglet.page("combobox-test")
page.horizontal_align = "stretch"
page.add(
    ComboBox(
        label="Your favorite color",
        value="c",
        options=[
            combobox.Option("RGB", item_type="header"),
            combobox.Option("red"),
            combobox.Option("green"),
            combobox.Option("blue"),
            combobox.Option("div1", item_type="divider"),
            combobox.Option("CMYK", item_type="header"),
            combobox.Option("c", "Cyan"),
            combobox.Option("m", "Magenta"),
            combobox.Option("y", "Yellow"),
            combobox.Option("k", "Black"),
        ],
    ),
    ComboBox(
        label="Your favorite car makers",
        multi_select=True,
        value="BMW, Volkswagen",
        width="50%",
        options=[
            combobox.Option("Select all", item_type="select_all"),
            combobox.Option("div1", item_type="divider"),
            combobox.Option("BMW"),
            combobox.Option("Toyota"),
            combobox.Option("Volkswagen"),
            combobox.Option("Mercedes-Benz"),
        ],
    ),
)
