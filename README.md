[![Build status](https://ci.appveyor.com/api/projects/status/863hk2g0yng7wvt6/branch/main?svg=true)](https://ci.appveyor.com/project/pglet/pglet-python/branch/main)

# Pglet - quickly build interactive web apps in Python

[Pglet](https://pglet.io) is a rich User Interface (UI) framework to quickly build interactive web apps in Python without prior knowledge of web technologies like HTTP, HTML, CSS or JavaSscript. You build UI with [controls](https://pglet.io/docs/reference/controls) which use [Fluent UI React](https://developer.microsoft.com/en-us/fluentui#/controls/web) to ensure your programs look cool and professional.

## Requirements

* Python 3.7 or above on Windows, Linux or macOS

## Installation

```
pip install pglet
```

## Hello, world!

```python
import pglet
from pglet import Text

p = pglet.page()
p.add(Text("Hello, world!"))
```

Run the sample above and a new browser window will pop up:

![Sample app in a browser](https://pglet.io/img/docs/quickstart-hello-world.png "Sample app in a browser")

Continue with [Python tutorial](https://pglet.io/docs/tutorials/python) demonstrating how to build a simple To-Do web app and share it on the internet.

Browse for more [Pglet examples](https://github.com/pglet/examples/tree/main/python).

Join to a conversation on [Pglet Discord server](https://discord.gg/rWjf7xx).