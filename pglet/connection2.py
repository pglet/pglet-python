import json
import re
import time
import threading
import uuid

from pglet.reconnecting_websocket import ReconnectingWebSocket
from .utils import is_windows, encode_attr
from .event import Event
from .protocol import *

# cmd = Command(0, "add", ["v1", "v2"])
# cmd.commands = [Command(1, "remove"), Command(1, "insert")]
# j = json.dumps(cmd, default=vars)

# cmd_dict = json.loads(j)
# cmd_object = Command(**cmd_dict)

# #print(j)
# print(cmd_object)

class Connection2:
    def __init__(self, ws: ReconnectingWebSocket):
        self.ws = ws
        self.ws.on_message = self._on_message
        self.ws_callbacks = {}

    def register_host_client(self, host_client_id: str, page_name: str, is_app: bool, auth_token: str, permissions: str):
        payload = RegisterHostClientRequestPayload(host_client_id, page_name, is_app, auth_token, permissions)
        result = self._send_message_with_result(Actions.REGISTER_HOST_CLIENT, payload)
        return RegisterHostClientResponsePayload(**result)

    def _on_message(self, data):
        print(f"_on_message: {data}")
        msg_dict = json.loads(data)
        msg = Message(**msg_dict)
        if msg.id != "":
            # callback
            evt = self.ws_callbacks[msg.id][0]
            self.ws_callbacks[msg.id] = (None, msg.payload)
            evt.set()
        else:
            print(msg.payload)

    def _send_message_with_result(self, action_name, payload):
        msg_id = uuid.uuid4().hex
        msg = Message(msg_id, action_name, payload)
        j = json.dumps(msg, default=vars)
        evt = threading.Event()
        self.ws_callbacks[msg_id] = (evt, None)
        self.ws.send(j)
        evt.wait()
        return self.ws_callbacks.pop(msg_id)[1]

# ============================================

    def __on_event(self, evt):
        pass

    def send_batch(self, commands):
        with self.lock:
            self.__send("begin")
            for command in commands:
                self.__send(command)
            result = self.__send("end")
            if result == "":
                return []
            else:
                return result.split('\n')

    def send(self, command):
        with self.lock:
            return self.__send(command)

    def __send(self, command):
        fire_and_forget = False
        cmdName = command.split(' ', 1)[0].strip()
        if cmdName[len(cmdName) - 1] == 'f' or cmdName.lower() == 'close':
            fire_and_forget = True

        if is_windows():
            return self.__send_windows(command, fire_and_forget)
        else:
            return self.__send_linux(command, fire_and_forget)

    def wait_event(self):
        self.event_available.clear()
        self.event_available.wait()
        return self.last_event

    def wait_close(self):
        while True:
            e = self.wait_event()
            if e.target == "page" and e.name == "close":
                break

    def __start_event_loop(self):
        thread = threading.Thread(target=self.__event_loop, daemon=True)
        thread.start()

    def __event_loop(self):
        while True:
            if is_windows():
                evts = self.__wait_events_windows()
            else:
                evts = self.__wait_events_linux()

            for e in evts:
                if e == None:
                    return                 

                if self.on_event != None:
                    self.on_event(e)

                if e.target == "page" and e.name == "close":
                    self.close()
                    return
                elif e.target != "page" or e.name != "change":
                    self.last_event = e
                    self.event_available.set()

    def __init_windows(self):
        self.win_command_pipe = open(rf'\\.\pipe\{self.conn_id}', 'r+b', buffering=0)
        self.win_event_pipe = open(rf'\\.\pipe\{self.conn_id}.events', 'r+b', buffering=0)

    def __send_windows(self, command, fire_and_forget):
        # send command
        self.win_command_pipe.write(command.encode('utf-8'))

        if fire_and_forget:
            return

        # wait for result
        r = self.win_command_pipe.readline().decode('utf-8').strip('\n')
        result_parts = re.split(r"\s", r, 1)
        if result_parts[0] == "error":
            raise Exception(result_parts[1])
        
        result = result_parts[1]
        extra_lines = int(result_parts[0])
        for _ in range(extra_lines):
            line = self.win_command_pipe.readline().decode('utf-8').strip('\n')
            result = result + "\n" + line
        return result

    def __wait_events_windows(self):
        r = self.win_event_pipe.readline().decode('utf-8').strip('\n')
        yield self.__parse_event_line(r)

    def __init_linux(self):
        pass

    def __send_linux(self, command, fire_and_forget):
        # send command
        pipe = open(rf'{self.conn_id}', "w")
        pipe.write(command)
        pipe.close()

        if fire_and_forget:
            return

        # wait for result
        pipe = open(rf'{self.conn_id}', "r")
        r = pipe.readline().strip('\n')
        result_parts = re.split(r"\s", r, 1)
        if result_parts[0] == "error":
            raise Exception(result_parts[1])
        
        result = result_parts[1]
        extra_lines = int(result_parts[0])
        for _ in range(extra_lines):
            line = pipe.readline().strip('\n')
            result = result + "\n" + line
        pipe.close()
        return result

    def __wait_events_linux(self):
        for line in open(rf'{self.conn_id}.events', "r"):
            yield self.__parse_event_line(line.strip('\n'))
    
    def __parse_event_line(self, line):
        if line == "":
            return None
        result_parts = re.split(r"\s", line, 2)
        return Event(result_parts[0], result_parts[1], result_parts[2])

    def close(self):
        if self.win_command_pipe != None:
            self.win_command_pipe.close()
        if self.win_event_pipe != None:
            self.win_event_pipe.close()