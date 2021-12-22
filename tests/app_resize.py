import json
import logging
import os,sys,inspect
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text

logging.basicConfig(level=logging.INFO)

def main(page):

  left_column = Stack(width='33%', height=40, bgcolor='Orange10', horizontal_align="center", vertical_align="center", controls=[Text("Column 1")])
  center_column = Stack(width='33%', height=40, bgcolor='CyanBlue10', horizontal_align="center", vertical_align="center", controls=[Text("Column 2")])
  right_column = Stack(width='33%', height=40, bgcolor='YellowGreen10', horizontal_align="center", vertical_align="center", controls=[Text("Column 3")])

  page.add(
      Stack(horizontal=True, wrap=True, gap=0, width='100%', bgcolor='#ddddee', horizontal_align="space-between", controls=[
          left_column,
          center_column,
          right_column
      ])
  )

  def page_resize(e):
      print('page_resize:', page.win_width, page.win_height)
      if page.win_width < 576:
          # small device
          left_column.width = center_column.width = right_column.width = '100%'
      elif page.win_width > 576 and page.win_width < 768:
          # medium device
          left_column.width = center_column.width = right_column.width = '50%'
          right_column.width = '100%'
      else:
          # device with a large screen
          left_column.width = center_column.width = right_column.width = '33.3%'
      page.update()

  page.on_resize = page_resize
  page_resize(None)

pglet.app("page-resize", target=main, web=False, no_window=False)
