# Pglet client for Python

[Pglet](https://pglet.io) (*"pagelet"*) is a rich user interface (UI) framework for programs written in Python or any other language. 
Pglet renders web UI, so you can easily [build web apps](https://pglet.io/docs/quickstart) with Python.
Knowledge of HTML/CSS/JavaScript is not required as you build UI with [controls](https://pglet.io/docs/reference/controls). Pglet controls are built with [Fluent UI React](https://developer.microsoft.com/en-us/fluentui#/controls/web) to ensure your programs look cool and professional.

## Hello, world!

```python
import pglet
from pglet import Text

p = pglet.page()
p.add(Text(value="Hello, world!"))
```

Run the sample above with Python 3 and in a new browser window you'll get:

![Sample app in a browser](https://pglet.io/img/docs/quickstart-hello-world.png "Sample app in a browser")

Read [Python tutorial](https://pglet.io/docs/tutorials/python) for further information and more examples.