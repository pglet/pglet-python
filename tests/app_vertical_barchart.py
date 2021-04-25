import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import random
import time

import pglet
from pglet import Text, VerticalBarChart
from pglet.verticalbarchart import Point

def main(page):

    # Vertical chart with textual x axis
    red_point = Point(x='Red', y=20, color='MediumOrchid', legend='Red', y_tooltip='20%')
    simple_chart = VerticalBarChart(tooltips=True, legend=True, width='50%', height=300,
        y_ticks=5, bar_width=20, y_format='{y}%', points=[
            red_point,
            Point(x='Green', y=50, color='LimeGreen', legend='Green', y_tooltip='50%'),
            Point(x='Blue', y=30, color='LightSkyBlue', legend='Blue', y_tooltip='30%')
        ]
    )

    # Vertical chart with numeric x axis
    num_chart = VerticalBarChart(y_ticks=5, y_min=0, y_max=100, y_format='{y}%', 
            width='100%', height=400, bar_width=20)

    page.add(
        Text("Vertical chart with textual x axis", size='xLarge'),
        simple_chart,

        Text("Vertical chart with numeric x axis", size='xLarge'),
        num_chart,
    )

    for v in range(21, 40):
        red_point.y = v
        page.update()
        time.sleep(0.01)

    for i in range(0, 100):
        num_chart.points.append(Point(x=i, y=round(random.random() * 100)))
        if len(num_chart.points) > 30:
            num_chart.points.pop(0)
        page.update()
        time.sleep(0.05)

pglet.app("pglet-verticallinechart", target=main)