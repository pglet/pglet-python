import re
from .utils import is_windows
from .event import Event

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

    def add(self, *controls, to=None, at=None):
        cmd = "add"

        if to:
            cmd += f" to=\"{to}\""

        if isinstance(at, int):
            cmd += f" at=\"{at}\""

        index = []

        for control in controls:
            if isinstance(control, list):
                for c in control:
                    cmd += f"\n{c.get_cmd_str(index=index)}"
            else:
                cmd += f"\n{control.get_cmd_str(index=index)}"

        result = self.send(cmd)
        ids = result.split(" ")

        for i in range(len(ids)):
            index[i].id = ids[i]

        if len(ids) == 1:
            return ids[0]
        else:
            return ids

    def update(self, *controls, fire_and_forget=False):
        cmd = "set"
        for control in controls:
            if isinstance(control, list):
                for c in control:
                    cmd += f"\n{c.get_cmd_str(update=True)}"
            else:
                cmd += f"\n{control.get_cmd_str(update=True)}"

    def set_value(self, id, value, fire_and_forget=False):
        pass

    def get_value(self, id):
        pass

    def show(self, *control_ids, fire_and_forget=False):
        pass

    def hide(self, *control_ids, fire_and_forget=False):
        pass

    def disable(self, *control_ids, fire_and_forget=False):
        pass

    def enable(self, *control_ids, fire_and_forget=False):
        pass

    def clean(self, *control_ids, fire_and_forget=False):
        pass

    def remove(self, at=None, *control_ids, fire_and_forget=False):
        pass
    
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