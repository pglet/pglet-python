import websocket
import threading, random, time

class ReconnectingWebSocket:
    def __init__(self, url) -> None:
        self.url = url
        self.on_open = None
        self.on_message = None
        self.connected = threading.Event()
        self.retry = 0
    
    def on_message(self, handler):
        self.on_message = handler
    
    def _on_open(self, wsapp) -> None:
        self.connected.set()
        self.retry = 0
        if self.on_open != None:
            self.on_open()

    def _on_message(self, wsapp, data) -> None:
        if self.on_message != None:
            self.on_message(data)

    def connect(self) -> None:
        self.wsapp = websocket.WebSocketApp(self.url, on_message=self._on_message, on_open=self._on_open)
        th = threading.Thread(target=self._connect_loop, args=(), daemon=True)
        th.start()
    
    def send(self, message) -> None:
        self.connected.wait()
        self.wsapp.send(message)

    def close(self) -> None:
        self.wsapp.close()

    # TODO: Can't do CTRL+C while it sleeps between re-connects
    # Change to Event: https://stackoverflow.com/questions/5114292/break-interrupt-a-time-sleep-in-python
    def _connect_loop(self):
        while True:
            print(f"Connecting Pglet Server at {self.url}...")
            r = self.wsapp.run_forever()
            self.connected.clear()
            if r != True:
                return
            backoff_in_seconds = 1
            sleep = (backoff_in_seconds * 2 ** self.retry + 
                    random.uniform(0, 1))
            print(f"Reconnecting Pglet Server in {sleep} seconds")
            time.sleep(sleep)

            self.retry += 1