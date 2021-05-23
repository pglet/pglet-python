import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Text, Spinner

def main(page):
    page.add(
        Text("Spinner sizes", size='xLarge'),
        Spinner("Extra small spinner", size='xSmall', label_position='left'),
        Spinner("Small spinner", size='small', label_position='left'),
        Spinner("Medium spinner", size='medium', label_position='left'),
        Spinner("Large spinner", size='large', label_position='left'),

        Text("Spinner label positioning", size='xLarge'),

        Text("Spinner with label positioned below"),
        Spinner("I am definitely loading...", label_position='Bottom'),

        Text("Spinner with label positioned above"),
        Spinner("Seriously, still loading...", label_position='Top'),

        Text("Spinner with label positioned to right"),
        Spinner("Wait, wait...", label_position='Right'),

        Text("Spinner with label positioned to left"),
        Spinner("Nope, still loading...", label_position='Left')
    )

pglet.app(target=main, local=True)