import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import pglet

from pglet import Page, Text, PieChart
from pglet import piechart

page = pglet.page("index")
page.update(Page(title="Hello, pglet!"))
page.clean()

t=Text("This is text")

pc = PieChart(legend=True, tooltips=True, inner_value=40, inner_radius=42, width='100%', data=[
                    piechart.P(value=20, color='yellow', legend='Yellow color', tooltip='20%'),
                    piechart.P(value=30, color='green', legend='Green color', tooltip='30%')])

page.add(t, pc)