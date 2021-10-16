import websocket
import threading, time

def on_message(wsapp, message):
    print(message)

def on_open(wsapp):
    print("Connection opened!")

def connect_loop(wsapp):
    while True:
        try:
            print("Connecting...")
            r = wsapp.run_forever()
        except Exception as e:
            #gc.collect()
            print("Websocket connection Error  : {0}".format(e))
        print("run_forever result", r)
        if r != True:
            return
        print("Reconnecting websocket after 5 sec")
        time.sleep(5)


wsapp = websocket.WebSocketApp("ws://127.0.0.1:5000/ws", on_message=on_message, on_open=on_open)
wst = threading.Thread(target=connect_loop, args=(wsapp,), daemon=True)
wst.start()

time.sleep(1)
wsapp.send("{ \"action\": \"test\" }")

input("Press Enter to exit...")

wsapp.close()