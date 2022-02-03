import pglet
from pglet import Text

page = pglet.page("hello-world")
page.title = "Hello, world!"
page.add(Text("Hello, world!"))
