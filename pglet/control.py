from .utils import encode_attr
from difflib import SequenceMatcher
import datetime as dt

class Control:
    def __init__(self, id=None, width=None, height=None,
            padding=None, margin=None, visible=None, disabled=None):
        self.__page = None
        self.__attrs = {}
        self.__previous_children = []
        self.id = id
        self.__gid = None
        if id == "page":
            self.__gid = "page"
        self.width = width
        self.height = height
        self.padding = padding
        self.margin = margin
        self.visible = visible
        self.disabled = disabled
        self.__event_handlers = {}

    def _get_children(self):
        return []

    def _get_control_name(self):
        raise Exception("_getControlName must be overridden in inherited class")

    def _add_event_handler(self, event_name, handler):
        self.__event_handlers[event_name] = handler

    def _get_event_handler(self, event_name):
        return self.__event_handlers.get(event_name)

    def _get_attr(self, name, defValue=None):
        if not name in self.__attrs:
            return defValue
        return self.__attrs[name][0]

    def _set_attr(self, name, value):
        if value == None:
            if name in self.__attrs:
                del self.__attrs[name]
            return
        self.__attrs[name] = (value, True)        

# event_handlers
    @property
    def event_handlers(self):
        return self.__event_handlers

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
    def visible(self, value):
        assert value == None or isinstance(value, bool), "visible must be a boolean"
        self._set_attr("visible", value)

# disabled
    @property
    def disabled(self):
        return self._get_attr("disabled")

    @disabled.setter
    def disabled(self, value):
        assert value == None or isinstance(value, bool), "disabled must be a boolean"
        self._set_attr("disabled", value)

# public methods
    def build_update_commands(self, index, added_controls, commands):
        update_attrs = self._get_cmd_attrs(update=True)

        if len(update_attrs) > 0:
            commands.append(f'set {" ".join(update_attrs)}')

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
                    self.__remove_control_recursively(index, ctrl)
                    ids.append(ctrl.__gid)
                commands.append(f'remove {" ".join(ids)}')
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
                    self.__remove_control_recursively(index, ctrl)
                    ids.append(ctrl.__gid)
                commands.append(f'remove {" ".join(ids)}')
                for h in current_ints[b1:b2]:
                    # add
                    ctrl = hashes[h]
                    cmd = ctrl.get_cmd_str(index=index,added_controls=added_controls)
                    commands.append(f"add to=\"{self.__gid}\" at=\"{n}\"\n{cmd}")                    
                    n += 1
            elif tag == "insert":
                # add
                for h in current_ints[b1:b2]:
                    ctrl = hashes[h]
                    cmd = ctrl.get_cmd_str(index=index,added_controls=added_controls)
                    commands.append(f"add to=\"{self.__gid}\" at=\"{n}\"\n{cmd}")     
                    n += 1
        
        self.__previous_children.clear()
        self.__previous_children.extend(current_children)

    def __remove_control_recursively(self, index, control):
        for child in control._get_children():
            self.__remove_control_recursively(index, child)
        
        if control.__gid in index:
            del index[control.__gid]

# private methods
    def get_cmd_str(self, indent='', index=None, added_controls=None):

        # remove control from index
        if self.__gid and index != None and self.__gid in index:
            del index[self.__gid]

        lines = []

        # main command
        parts = []

        # control name
        parts.append(indent + self._get_control_name())
        
        # base props
        attrParts = self._get_cmd_attrs(update=False)

        if len(attrParts) > 0:
            parts.extend(attrParts)
            lines.append(" ".join(parts))

        if added_controls != None:
            added_controls.append(self)

        # controls
        children = self._get_children()
        for control in children:
            childCmd = control.get_cmd_str(indent=indent+"  ", index=index, added_controls=added_controls)
            if childCmd != "":
                lines.append(childCmd)

        self.__previous_children.clear()
        self.__previous_children.extend(children)

        return "\n".join(lines)

    def _get_cmd_attrs(self, update=False):
        parts = []

        if update and not self.__gid:
            return parts

        for attrName in sorted(self.__attrs):
            dirty = self.__attrs[attrName][1]

            if attrName == "id":
                continue

            if update and not dirty:
                continue

            val = self.__attrs[attrName][0]
            sval = ""
            if isinstance(val, bool):
                sval = str(val).lower()
            elif isinstance(val, dt.datetime) or isinstance(val, dt.date):
                sval = val.isoformat()
            else:
                sval = encode_attr(val)

            parts.append(f'{attrName}="{sval}"')
            self.__attrs[attrName] = (val, False)

        id = self.__attrs.get("id")
        if not update and id != None:
            parts.insert(0, f'id="{encode_attr(id[0])}"')
        elif update and len(parts) > 0:
            parts.insert(0, f'"{encode_attr(self.__gid)}"')
        
        return parts