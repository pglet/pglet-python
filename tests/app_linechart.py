import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import datetime
import random
import time

import pglet
from pglet import Text, LineChart
from pglet.linechart import Data, Point

def main(page):

    # simple line chart with numbers on X axis
    simple_chart = LineChart(legend=True, tooltips=True, stroke_width=4, y_min=0, y_max=100, y_format='{y}%', 
            x_type='number', width='30%', height='300px', lines=[
                Data(legend='Line 1', points=[
                    Point(x=0, y=0),
                    Point(x=1, y=10),
                    Point(x=2, y=20),
                    Point(x=3, y=50),
                    Point(x=4, y=100),
                    Point(x=5, y=90),
                    Point(x=6, y=50),
                    Point(x=7, y=30),
                    Point(x=8, y=20),
                    Point(x=9, y=5)
                ])
            ])

    # two lines on the same chart
    multi_chart = LineChart(legend=True, tooltips=True, stroke_width=4, y_ticks=5, y_min=0, y_max=100, y_format='{y}%', 
            x_type='number', width='30%', height='400px', lines=[])

    line1 = Data(legend='Line 1', color='Orange')
    line2 = Data(legend='Line 2', color='Magenta')
    for i in range (0, 21):
        line1.points.append(Point(x=i, y=random.random() * 100))
        line2.points.append(Point(x=i, y=random.random() * 100))
    multi_chart.lines.append(line1)
    multi_chart.lines.append(line2)

    # negative values with time on X axis
    temp_chart = LineChart(legend=True, tooltips=True, y_ticks=4, y_min=-20, y_max=20, y_format='{y} °C', 
            x_type='date', width='500px', height='400px', lines=[
                Data(color='green', legend='t, °C')
            ])
    start_date = datetime.datetime(2021, 4, 1, 10, 5)
    m = 0
    for i in range(0, 60):
        d = start_date + datetime.timedelta(minutes=m)
        v = round((random.random() - 0.5) * 40)
        temp_chart.lines[0].points.append(Point(x=d, y=v))
        m += 1

    page.add(
        Text("Simple line chart with numbers on X axis", size='xLarge'),
        simple_chart,

        Text("Line chart with two lines", size='xLarge'),
        multi_chart,

        Text("Negative values with time on X axis", size='xLarge'),
        temp_chart        
    )

    # simulate "running" chart
    while(True):
        d = start_date + datetime.timedelta(minutes=m)
        v = round((random.random() - 0.5) * 40)
        temp_chart.lines[0].points.pop(0)
        temp_chart.lines[0].points.append(Point(x=d, y=v))    
        m += 1
        page.update()
        time.sleep(1)

pglet.app("pglet-linechart", target=main)