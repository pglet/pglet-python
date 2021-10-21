import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import time
from pglet import reconnecting_websocket


exit()



def on_message(message):
    print(message)

def on_open():
    print("Connection opened!")

rws = reconnecting_websocket.ReconnectingWebSocket("ws://localhost:5000/ws", on_open, on_message)
rws.connect()

time.sleep(1)
rws.send("{ \"action\": \"test\" }")

try:
    input("Press Enter to exit...")
except (Exception, KeyboardInterrupt, SystemExit) as e:
    print ("Interrupted!")

rws.close()