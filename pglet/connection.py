import re
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

    def __init__(self, conn_id):
        self.conn_id = conn_id

        if is_windows():
            self.__init_windows()
        else:
            self.__init_linux()

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
            return ids[0]
        else:
            return ids

    def update(self, *controls, fire_and_forget=False):
        cmd = "set"
        if fire_and_forget:
            cmd = "setf"

        for control in controls:
            if isinstance(control, list):
                for c in control:
                    cmd += f"\n{c.get_cmd_str(update=True)}"
            else:
                cmd += f"\n{control.get_cmd_str(update=True)}"

        self.send(cmd)

    def set_value(self, id, value, fire_and_forget=False):
        cmd = "set"
        if fire_and_forget:
            cmd = "setf"

        self.send(f'{cmd} {id} value="{encode_attr(value)}"')

    def get_value(self, id):
        return self.send(f'get {id} value')

    def show(self, *control_ids, fire_and_forget=False):
        self.send(self._build_set_cmd('visible="true"', fire_and_forget, *control_ids))

    def hide(self, *control_ids, fire_and_forget=False):
        self.send(self._build_set_cmd('visible="false"', fire_and_forget, *control_ids))

    def disable(self, *control_ids, fire_and_forget=False):
        self.send(self._build_set_cmd('disabled="true"', fire_and_forget, *control_ids))

    def enable(self, *control_ids, fire_and_forget=False):
        self.send(self._build_set_cmd('disabled="false"', fire_and_forget, *control_ids))

    def _build_set_cmd(self, propValue, fire_and_forget, *control_ids):
        cmd = 'set'
        if fire_and_forget:
            cmd = 'setf'

        lines = [cmd]
        for id in control_ids:
            lines.append(f"{id} {propValue}")

        #raise Exception(type(control_ids))
        #raise Exception("\n".join(lines))
        return "\n".join(lines)

    def clean(self, *control_ids, fire_and_forget=False):
        cmd = 'clean'
        if fire_and_forget:
            cmd = 'cleanf'
        self.send(f'{cmd} {" ".join(control_ids)}')

    def remove(self, *control_ids, fire_and_forget=False):
        cmd = 'remove'
        if fire_and_forget:
            cmd = 'removef'
        self.send(f'{cmd} {" ".join(control_ids)}')
    
    def send(self, command):
        if is_windows():
            return self.__send_windows(command)
        else:
            return self.__send_linux(command)

    def wait_event(self):
        if is_windows():
            return self.__wait_event_windows()
        else:
            return self.__wait_event_linux()

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