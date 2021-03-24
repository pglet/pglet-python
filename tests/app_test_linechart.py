import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import pglet
import datetime as dt

from pglet import Page, Text, LineChart
from pglet import linechart

page = pglet.page("index")
page.update(Page(title="Hello, pglet!"))
page.clean()

t=Text("This is text")

date1 = dt.date(2000, 2, 3)
date2 = dt.date(2001, 5, 17)
date3 = dt.date(2003, 7, 5)
date4 = dt.date(2004, 7, 19)

lc = LineChart(legend=True, tooltips=True, stroke_width=4, y_min=0, y_max=100, y_ticks=2, y_format='{y}%', 
                x_type='date', datas=[
                    linechart.Data(color='yellow', legend='yellow color', points=[
                        linechart.P(x=date1, y=100),
                        linechart.P(x=date2, y=50)]),
                    linechart.Data(color='green', legend='green color', points=[
                        linechart.P(x=date3, y=20),
                        linechart.P(x=date4, y=10)])
                ])


page.add(t, lc)