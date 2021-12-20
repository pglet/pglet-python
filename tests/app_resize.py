import json
import os,sys,inspect
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

def main(page):

  left_column = Stack(width='30%', height=40, bgcolor='CyanBlue10')
  center_column = Stack(width='30%', height=40, bgcolor='CyanBlue10')
  right_column = Stack(width='30%', height=40, bgcolor='CyanBlue10')

  page.add(
      Stack(horizontal=True, wrap=True, gap=20, width='100%', bgcolor='#ddddee', controls=[
          left_column,
          center_column,
          right_column
      ])
  )

  def page_resize(e):
      if page.width < 576:
          # small device
          left_column.width = center_column.width = right_column.width = '100%'
      else:
          # device with a large screen
          left_column.width = center_column.width = right_column.width = '30%'
      page.update()

  page.on_resize = page_resize


pglet.app("page-resize", target=main, web=False)
