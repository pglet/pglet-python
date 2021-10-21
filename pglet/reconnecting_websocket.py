import websocket
import threading, time

class ReconnectingWebSocket:
    def __init__(self, url, on_open, on_message) -> None:
        self.url = url
        self.on_open = on_open
        self.on_message = on_message

    def connect(self) -> None:
        self.wsapp = websocket.WebSocketApp(self.url, on_message=self.on_message, on_open=self.on_open)
        th = threading.Thread(target=self._connect_loop, args=(), daemon=True)
        th.start()
    
    def send(self, message) -> None:
        self.wsapp.send(message)

    def close(self) -> None:
        self.wsapp.close()

    def _connect_loop(self):
        while True:
            try:
                print("Connecting...")
                r = self.wsapp.run_forever()
            except (Exception, KeyboardInterrupt, SystemExit) as e:
                #gc.collect()
                print("Websocket connection Error  : {0}".format(e))
            print("run_forever result", r)
            if r != True:
                return
            print("Reconnecting websocket after 5 sec")
            time.sleep(5)