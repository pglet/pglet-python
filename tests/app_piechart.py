import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import datetime
import random
import time

import pglet
from pglet import Text, PieChart
from pglet.piechart import Point

def main(page):

    # simple donut-like pie chart
    chart1 = PieChart(width='50%', inner_radius=40, inner_value=42, points=[
        Point(color='yellow', value=10),
        Point(color='green', value=32)
    ])

    # pie chart with legent
    chart2 = PieChart(width='50%', legend=True, tooltips=True, points=[
        Point(legend='Free space', value=10, tooltip='10%'),
        Point(legend='Total space', value=20, tooltip='20%'),
        Point(legend='Reserved space', value=30, tooltip='30%'),
        Point(legend='A:', value=20, tooltip='20%'),
        Point(legend='B:', value=20, tooltip='20%'),
        Point(legend='C:', value=20, tooltip='20%')
    ])    

    page.add(
        Text("Donut-like PieChart", size='xLarge'),
        chart1,

        Text("PieChart with legend and tooltips", size='xLarge'),
        chart2        
    )

pglet.app("pglet-piechart", target=main)