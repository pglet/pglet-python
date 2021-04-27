import os

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text

def main(page):
    
    page.add(
        Text('Squares', size='large'),
        Stack(horizontal=True, controls=[
            Text('left top', align='left', vertical_align='top', width=100, height=100, bgcolor='salmon', color='white', padding=5),
            Text('center top', align='center', vertical_align='top', width=100, height=100, bgcolor='salmon', color='white', padding=5, size='large', border='1px solid #555'),
            Text('right top', align='right', vertical_align='top', width=100, height=100, bgcolor='salmon', color='white', padding=5, border='2px solid #555')
        ]),
        Stack(horizontal=True, controls=[
            Text('left center', align='left', vertical_align='center', width=100, height=100, bgcolor='PaleGoldenrod', padding=5),
            Text('center center', align='center', vertical_align='center', width=100, height=100, bgcolor='PaleGoldenrod', padding=5, size='large', border='1px solid #555'),
            Text('right center', align='right', vertical_align='center', width=100, height=100, bgcolor='PaleGoldenrod', padding=5, border='2px solid #555')
        ]),
        Stack(horizontal=True, controls=[
            Text('left bottom', align='left', vertical_align='center', width=100, height=100, bgcolor='PaleGreen', padding=5),
            Text('center bottom', align='center', vertical_align='center', width=100, height=100, bgcolor='PaleGreen', padding=5, size='large', border='1px solid #555'),
            Text('right bottom', align='right', vertical_align='center', width=100, height=100, bgcolor='PaleGreen', padding=5, border='2px solid #555')
        ]),
        Text('Circles', size='large'),
        Stack(horizontal=True, controls=[
            Text('regular', align='center', vertical_align='center', width=100, height=100, border_radius=50, bgcolor='salmon'),
            Text('bold italic', bold=True, italic=True, align='center', vertical_align='center', width=100, height=100, border_radius=50, bgcolor='PaleGoldenrod', size='large', border='1px solid #555'),
            Text('bold', bold=True, align='center', vertical_align='center', width=100, height=100, border_radius=50, bgcolor='PaleGreen', border='2px solid #555')
        ]),
        Text('Markdown', size='large'),
        Text('''
# GitHub Flavored Markdown

## Autolink literals

www.example.com, https://example.com, and contact@example.com.

## Strikethrough

~one~ or ~~two~~ tildes.

### Code sample

```
import pglet
page = page.page()
```

## Table

| a | b  |  c |  d  |
| - | :- | -: | :-: |

## Tasklist

* [ ] to do
* [x] done

        ''', markdown=True)
    )

pglet.app("python-text", target=main)