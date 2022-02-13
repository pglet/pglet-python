import datetime as dt
import threading
from typing import Optional
from difflib import SequenceMatcher

try:
    from typing import Literal
except:
    from typing_extensions import Literal

from beartype import beartype

from pglet.protocol import Command

BorderStyle = Literal[
    None, "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"
]

TextSize = Literal[
    None,
    "tiny",
    "xSmall",
    "small",
    "smallPlus",
    "medium",
    "mediumPlus",
    "large",
    "xLarge",
    "xxLarge",
    "superLarge",
    "mega",
]

TextAlign = Literal[None, "left", "right", "center", "justify"]


class Control:
    def __init__(
        self,
        id=None,
        width=None,
        height=None,
        padding=None,
        margin=None,
        visible=None,
        disabled=None,
        data=None,
    ):
        self.__page = None
        self.__attrs = {}
        self.__previous_children = []
        self.id = id
        self.__uid = None
        if id == "page":
            self.__uid = "page"
        self.width = width
        self.height = height
        self.padding = padding
        self.margin = margin
        self.visible = visible
        self.disabled = disabled
        self.data = data
        self.__event_handlers = {}
        self._lock = threading.Lock()

    def _get_children(self):
        return []

    def _get_control_name(self):
        raise Exception("_getControlName must be overridden in inherited class")

    def _add_event_handler(self, event_name, handler):
        self.__event_handlers[event_name] = handler

    def _get_event_handler(self, event_name):
        return self.__event_handlers.get(event_name)

    def _get_attr(self, name, def_value=None, data_type="string"):
        name = name.lower()
        if not name in self.__attrs:
            return def_value

        s_val = self.__attrs[name][0]
        if data_type == "bool" and s_val != None and isinstance(s_val, str):
            return s_val.lower() == "true"
        elif data_type == "float" and s_val != None and isinstance(s_val, str):
            return float(s_val)
        else:
            return s_val

    def _set_attr(self, name, value, dirty=True):
        self._set_attr_internal(name, value, dirty)

    def _set_attr_internal(self, name, value, dirty=True):
        name = name.lower()
        orig_val = self.__attrs.get(name)

        if orig_val == None and value == None:
            return

        if value == None:
            value = ""

        if orig_val == None or orig_val[0] != value:
            self.__attrs[name] = (value, dirty)

    # event_handlers
    @property
    def event_handlers(self):
        return self.__event_handlers

    # _previous_children
    @property
    def _previous_children(self):
        return self.__previous_children

    # page
    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, page):
        self.__page = page

    # id
    @property
    def id(self):
        return self._get_attr("id")

    # uid
    @property
    def uid(self):
        return self.__uid

    @id.setter
    def id(self, value):
        self._set_attr("id", value)

    # width
    @property
    def width(self):
        return self._get_attr("width")

    @width.setter
    def width(self, value):
        self._set_attr("width", value)

    # height
    @property
    def height(self):
        return self._get_attr("height")

    @height.setter
    def height(self, value):
        self._set_attr("height", value)

    # padding
    @property
    def padding(self):
        return self._get_attr("padding")

    @padding.setter
    def padding(self, value):
        self._set_attr("padding", value)

    # margin
    @property
    def margin(self):
        return self._get_attr("margin")

    @margin.setter
    def margin(self, value):
        self._set_attr("margin", value)

    # visible
    @property
    def visible(self):
        return self._get_attr("visible")

    @visible.setter
    @beartype
    def visible(self, value: Optional[bool]):
        self._set_attr("visible", value)

    # disabled
    @property
    def disabled(self):
        return self._get_attr("disabled")

    @disabled.setter
    @beartype
    def disabled(self, value: Optional[bool]):
        self._set_attr("disabled", value)

    # data
    @property
    def data(self):
        return self._get_attr("data")

    @data.setter
    def data(self, value):
        self._set_attr("data", value)

    # public methods
    def update(self):
        if not self.__page:
            raise Exception("Control must be added to the page first.")
        self.__page.update(self)

    def clean(self):
        with self._lock:
            self._previous_children.clear()
            for child in self._get_children():
                self._remove_control_recursively(self.__page.index, child)
            return self.__page._send_command("clean", [self.uid])

    def build_update_commands(self, index, added_controls, commands):
        update_cmd = self._get_cmd_attrs(update=True)

        if len(update_cmd.attrs) > 0:
            update_cmd.name = "set"
            commands.append(update_cmd)

        # go through children
        previous_children = self.__previous_children
        current_children = self._get_children()

        hashes = {}
        previous_ints = []
        current_ints = []

        for ctrl in previous_children:
            hashes[hash(ctrl)] = ctrl
            previous_ints.append(hash(ctrl))

        for ctrl in current_children:
            hashes[hash(ctrl)] = ctrl
            current_ints.append(hash(ctrl))

        # print("previous_ints:", previous_ints)
        # print("current_ints:", current_ints)

        sm = SequenceMatcher(None, previous_ints, current_ints)

        n = 0
        for tag, a1, a2, b1, b2 in sm.get_opcodes():
            if tag == "delete":
                # deleted controls
                ids = []
                for h in previous_ints[a1:a2]:
                    ctrl = hashes[h]
                    self._remove_control_recursively(index, ctrl)
                    ids.append(ctrl.__uid)
                commands.append(Command(0, "remove", ids, None, None, None))
            elif tag == "equal":
                # unchanged control
                for h in previous_ints[a1:a2]:
                    ctrl = hashes[h]
                    ctrl.build_update_commands(index, added_controls, commands)
                    n += 1
            elif tag == "replace":
                ids = []
                for h in previous_ints[a1:a2]:
                    # delete
                    ctrl = hashes[h]
                    self._remove_control_recursively(index, ctrl)
                    ids.append(ctrl.__uid)
                commands.append(Command(0, "remove", ids, None, None, None))
                for h in current_ints[b1:b2]:
                    # add
                    ctrl = hashes[h]
                    innerCmds = ctrl.get_cmd_str(
                        index=index, added_controls=added_controls
                    )
                    commands.append(
                        Command(
                            0,
                            "add",
                            None,
                            {"to": self.__uid, "at": str(n)},
                            None,
                            innerCmds,
                        )
                    )
                    n += 1
            elif tag == "insert":
                # add
                for h in current_ints[b1:b2]:
                    ctrl = hashes[h]
                    innerCmds = ctrl.get_cmd_str(
                        index=index, added_controls=added_controls
                    )
                    commands.append(
                        Command(
                            0,
                            "add",
                            None,
                            {"to": self.__uid, "at": str(n)},
                            None,
                            innerCmds,
                        )
                    )
                    n += 1

        self.__previous_children.clear()
        self.__previous_children.extend(current_children)

    def _remove_control_recursively(self, index, control):
        for child in control._get_children():
            self._remove_control_recursively(index, child)

        if control.__uid in index:
            del index[control.__uid]

    # private methods
    def get_cmd_str(self, indent=0, index=None, added_controls=None):

        # remove control from index
        if self.__uid and index != None and self.__uid in index:
            del index[self.__uid]

        commands = []

        # main command
        command = self._get_cmd_attrs(False)
        command.indent = indent
        command.values.append(self._get_control_name())
        commands.append(command)

        if added_controls != None:
            added_controls.append(self)

        # controls
        children = self._get_children()
        for control in children:
            childCmd = control.get_cmd_str(
                indent=indent + 2, index=index, added_controls=added_controls
            )
            commands.extend(childCmd)

        self.__previous_children.clear()
        self.__previous_children.extend(children)

        return commands

    def _get_cmd_attrs(self, update=False):
        command = Command(0, None, [], {}, [], [])

        if update and not self.__uid:
            return command

        for attrName in sorted(self.__attrs):
            attrName = attrName.lower()
            dirty = self.__attrs[attrName][1]

            if (update and not dirty) or attrName == "id":
                continue

            val = self.__attrs[attrName][0]
            sval = ""
            if val == None:
                continue
            elif isinstance(val, bool):
                sval = str(val).lower()
            elif isinstance(val, dt.datetime) or isinstance(val, dt.date):
                sval = val.isoformat()
            else:
                sval = str(val)
            command.attrs[attrName] = sval
            self.__attrs[attrName] = (val, False)

        id = self.__attrs.get("id")
        if not update and id != None:
            command.attrs["id"] = id
        elif update and len(command.attrs) > 0:
            command.values.append(self.__uid)

        return command
