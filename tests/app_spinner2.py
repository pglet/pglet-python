import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Stack, Text, Spinner

page = pglet.page(local=True)

stack = Stack(width='50%', controls=[
    Text("Spinner label positioning", size='xLarge'),

    Text("Spinner with label positioned below"),
    Spinner("I am definitely loading...", label_position='Bottom'),

    Text("Spinner with label positioned above"),
    Spinner("Seriously, still loading...", label_position='Top'),

    Text("Spinner with label positioned to right"),
    Spinner("Wait, wait...", label_position='Right'),

    Text("Spinner with label positioned to left"),
    Spinner("Nope, still loading...", label_position='Left')
])

page.add(stack)