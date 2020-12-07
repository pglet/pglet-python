import re
import threading
from .utils import is_windows, encode_attr
from .event import Event
from .control import Control

class Connection:
    conn_id = ""
    url = ""
    web = False
    private = False

    win_command_pipe = None
    win_event_pipe = None

    event_available = threading.Event()
    last_event = None

    def __init__(self, conn_id):
        self.conn_id = conn_id

        if is_windows():
            self.__init_windows()
        else:
            self.__init_linux()

        self.__start_event_loop()

    def add(self, *controls, to=None, at=None, fire_and_forget=False):
        cmd = "add"
        if fire_and_forget:
            cmd = "addf"

        if to != None:
            cmd += f' to="{self._get_control_id(to)}"'

        if at != None:
            assert isinstance(at, int), "at must be an int"
            cmd += f' at="{at}"'

        index = []

        for control in controls:
            if isinstance(control, list):
                for c in control:
                    cmd += f"\n{c.get_cmd_str(index=index)}"
            else:
                cmd += f"\n{control.get_cmd_str(index=index)}"

        result = self.send(cmd)

        if fire_and_forget:
            return
        
        ids = result.split(" ")

        for i in range(len(ids)):
            index[i].id = ids[i]

        if len(ids) == 1:
            return index[0]
        else:
            return index

    def update(self, *controls, fire_and_forget=False):
        cmd = "set"
        if fire_and_forget:
            cmd = "setf"

        lines = []

        for control in controls:
            if isinstance(control, list):
                for c in control:
                    lines.append(c.get_cmd_str(update=True))
            else:
                lines.append(control.get_cmd_str(update=True))

        if len(lines) == 0:
            return

        slines = "\n".join(lines)
        self.send(f'{cmd}\n{slines}')

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
            parts.append(self._get_control_id(c))
        self.send(" ".join(parts))
    
    def send(self, command):
        if is_windows():
            return self.__send_windows(command)
        else:
            return self.__send_linux(command)

    def wait_event(self):
        self.event_available.wait()
        evt = self.last_event
        self.event_available.clear()
        return evt

    def __start_event_loop(self):
        thread = threading.Thread(target=self.__event_loop)
        thread.start()

    def __event_loop(self):
        while True:
            if is_windows():
                self.last_event = self.__wait_event_windows()
            else:
                self.last_event = self.__wait_event_linux()
            self.event_available.set()

    def __init_windows(self):
        self.win_command_pipe = open(rf'\\.\pipe\{self.conn_id}', 'r+b', buffering=0)
        self.win_event_pipe = open(rf'\\.\pipe\{self.conn_id}.events', 'r+b', buffering=0)

    def __send_windows(self, command):
        self.win_command_pipe.write(command.encode('utf-8'))
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

    def __send_linux(self, command):
        pipe = open(rf'{self.conn_id}', "w")
        pipe.write(command)
        pipe.close()

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