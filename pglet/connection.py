import re
import time
import threading
from .utils import is_windows, encode_attr
from .event import Event
from .control import Control

class Connection:
    def __init__(self, conn_id):
        self.conn_id = conn_id
        self.lock = threading.Lock()

        self.url = ""
        self.web = False
        self.private = False

        self.win_command_pipe = None
        self.win_event_pipe = None

        self.event_available = threading.Event()
        self.last_event = None
        self._event_handlers = {}        

        if is_windows():
            self.__init_windows()
        else:
            self.__init_linux()

        self.__start_event_loop()

    def add(self, *controls, to=None, at=None, trim=None, fire_and_forget=False):
        cmd = "add"
        if fire_and_forget:
            cmd = "addf"
        return self._add_or_replace(cmd, *controls, to=to, at=at, trim=trim, fire_and_forget=fire_and_forget)

    def replace(self, *controls, to=None, at=None, trim=None, fire_and_forget=False):
        cmd = "replace"
        if fire_and_forget:
            cmd = "replacef"
        return self._add_or_replace(cmd, *controls, to=to, at=at, trim=trim, fire_and_forget=fire_and_forget)

    def _add_or_replace(self, cmdName, *controls, to=None, at=None, trim=None, fire_and_forget=False):
        cmd = cmdName

        if to != None:
            cmd += f' to="{self._get_control_id(to)}"'

        if at != None:
            assert isinstance(at, int), "at must be an int"
            cmd += f' at="{at}"'

        if trim != None:
            assert isinstance(trim, int), "trim must be an int"
            cmd += f' trim="{trim}"'

        index = []

        for control in self._expand_controls_argv(*controls):
            if control.id:
                self._remove_event_handlers(control.id)
            cmd += f"\n{control.get_cmd_str(index=index, conn=self)}"

        result = self.send(cmd)

        if fire_and_forget:
            return
        
        ids = result.split(" ")

        for i in range(len(ids)):
            index[i].id = ids[i]

            # resubscribe event handlers
            event_handlers = index[i]._get_event_handlers()
            for event_name in event_handlers:
                self._add_event_handler(ids[i], event_name, event_handlers[event_name])

        if len(ids) == 1:
            return index[0]
        else:
            return index

    def update(self, *controls, fire_and_forget=False):
        cmd = "set"
        if fire_and_forget:
            cmd = "setf"

        lines = []

        for control in self._expand_controls_argv(*controls):
            lines.append(control.get_cmd_str(update=True))

        if len(lines) == 0:
            return

        slines = "\n".join(lines)
        self.send(f'{cmd}\n{slines}')

    def _expand_controls_argv(self, *controls):
        for control in controls:
            if isinstance(control, list):
                for c in control:
                    yield c
            else:
                yield control

    def set_value(self, id_or_control, value, fire_and_forget=False):
        cmd = "set"
        if fire_and_forget:
            cmd = "setf"

        self.send(f'{cmd} {self._get_control_id(id_or_control)} value="{encode_attr(value)}"')

    def get_value(self, id_or_control):
        return self.send(f'get {self._get_control_id(id_or_control)} value')

    def append_value(self, id_or_control, value, fire_and_forget=False):
        cmd = "append"
        if fire_and_forget:
            cmd = "appendf"

        self.send(f'{cmd} {self._get_control_id(id_or_control)} value="{encode_attr(value)}"')

    def show(self, *id_or_controls, fire_and_forget=False):
        self.send(self._build_set_cmd('visible="true"', fire_and_forget, *id_or_controls))

    def hide(self, *id_or_controls, fire_and_forget=False):
        self.send(self._build_set_cmd('visible="false"', fire_and_forget, *id_or_controls))

    def disable(self, *id_or_controls, fire_and_forget=False):
        self.send(self._build_set_cmd('disabled="true"', fire_and_forget, *id_or_controls))

    def enable(self, *id_or_controls, fire_and_forget=False):
        self.send(self._build_set_cmd('disabled="false"', fire_and_forget, *id_or_controls))

    def _build_set_cmd(self, propValue, fire_and_forget, *id_or_controls):
        cmd = 'set'
        if fire_and_forget:
            cmd = 'setf'

        lines = [cmd]
        for c in id_or_controls:
            lines.append(f"{self._get_control_id(c)} {propValue}")
        return "\n".join(lines)

    def clean(self, *id_or_controls, at=None, fire_and_forget=False):
        parts = []
        if not fire_and_forget:
            parts.append('clean')
        else:
            parts.append('cleanf')
        if at != None:
            assert isinstance(at, int), "at must be an int"
            parts.append(f'at="{at}"')
        for c in id_or_controls:
            parts.append(self._get_control_id(c))
        self.send(" ".join(parts))

    def remove(self, *id_or_controls, at=None, fire_and_forget=False):
        parts = []
        if not fire_and_forget:
            parts.append('remove')
        else:
            parts.append('removef')
        if at != None:
            assert isinstance(at, int), "at must be an int"
            parts.append(f'at="{at}"')
        for c in id_or_controls:
            control_id = self._get_control_id(c)
            parts.append(control_id)
            if at == None:
                self._remove_event_handlers(control_id)
        
        self.send(" ".join(parts))
    
    def send(self, command):

        fire_and_forget = False
        cmdName = command.split(' ', 1)[0].strip()
        if cmdName[len(cmdName) - 1] == 'f':
            fire_and_forget = True

        with self.lock:
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
                evt = self.__wait_event_windows()
            else:
                evt = self.__wait_event_linux()

            # call all event handlers
            control_events = self._event_handlers.get(evt.target)
            if control_events:
                handler = control_events.get(evt.name)
                if handler:
                    t = threading.Thread(target=handler, args=(evt,), daemon=True)
                    t.start()
            
            # release wait_event() loop
            #print ("EVENT:", evt.target, evt.name, evt.data)
            self.last_event = evt
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

    def __wait_event_windows(self):
        r = self.win_event_pipe.readline().decode('utf-8').strip('\n')
        result_parts = re.split(r"\s", r, 2)
        return Event(result_parts[0], result_parts[1], result_parts[2])

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

    def __wait_event_linux(self):
        pipe = open(rf'{self.conn_id}.events', "r")
        r = pipe.readline().strip('\n')
        pipe.close()
        result_parts = re.split(r"\s", r, 2)
        return Event(result_parts[0], result_parts[1], result_parts[2])        

    def close(self):
        raise Exception("Not implemented yet")

    def _get_control_id(self, id_or_control):
        result = ""
        if isinstance(id_or_control, Control):
            result = id_or_control.id
        elif isinstance(id_or_control, str):
            result = id_or_control
        else:
            result = str(id_or_control)
        if result == "":
            raise Exception("control ID cannot be empty")
        return result

    def _add_event_handler(self, control_id, event_name, handler):
        control_events = self._event_handlers.get(control_id)
        if not control_events:
            control_events = {}
            self._event_handlers[control_id] = control_events
        control_events[event_name] = handler

    def _remove_event_handlers(self, control_id):
        if control_id in self._event_handlers:
            del self._event_handlers[control_id]