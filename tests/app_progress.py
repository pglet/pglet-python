import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import time
import pglet
from pglet import Text, Progress

def main(page):
    page.add(
        Text("Indeterminate Progress", size='xLarge'),
        Progress("Operation progress", description="Doing something indefinite...", width='30%')
    )

    prog1 = Progress("Copying file1.txt to file2.txt", value=0, width='30%')
    page.add(
        Text("Default Progress", size='xLarge'),
        prog1
    )

    for i in range(0, 101):
        prog1.value = i
        prog1.update()
        time.sleep(0.005)

    prog2 = Progress("Provisioning your account", value=0, width='30%')
    page.add(
        prog2
    )

    prog2.description = "Preparing environment..."
    prog2.value = 0
    prog2.update()
    time.sleep(2)

    prog2.description = "Collecting information..."
    prog2.value = 20
    prog2.update()
    time.sleep(2)

    prog2.description = "Creatring database entities..."
    prog2.value = 40
    prog2.update()
    time.sleep(2)

    prog2.description = "Verifying the data..."
    prog2.value = 60
    prog2.update()
    time.sleep(2)

    prog2.description = "Finishing the process, almost done..."
    prog2.value = 80
    prog2.update()
    time.sleep(2)

    prog2.description = "Your account has been created!"
    prog2.value = 100
    prog2.update()


pglet.app("pglet-progress", target=main, local=True)