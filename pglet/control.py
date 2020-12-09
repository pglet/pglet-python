from .utils import encode_attr

class Control:
    def __init__(self, id=None, width=None, height=None,
            padding=None, margin=None, visible=None, disabled=None):
        self._conn = None
        self._attrs = {}
        self._id = id
        self.width = width
        self.height = height
        self.padding = padding
        self.margin = margin
        self.visible = visible
        self.disabled = disabled
        self._event_handlers = {}

    def _getChildren(self):
        return []

    def _getControlName(self):
        raise Exception("_getControlName must be overridden in inherited class")

    def _get_event_handlers(self):
        return self._event_handlers

    def _add_event_handler(self, event_name, handler):
        # add handler to the control handlers list (for rebinding on control changes)
        event_group = self._event_handlers.get(event_name)
        if not event_group:
            event_group = {}
            self._event_handlers[event_name] = event_group
        event_group[handler] = True

        # add handler to the connection if control is already added
        if self._conn:
            self._conn._add_event_handler(self._id, event_name, handler)

# id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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

# private methods
    def _get_attr(self, name, defValue=None):
        if not name in self._attrs:
            return defValue
        return self._attrs[name][0]

    def _set_attr(self, name, value):
        if value == None:
            if name in self._attrs:
                del self._attrs[name]
            return
        self._attrs[name] = (value, True)

    def get_cmd_str(self, update=False, indent='', index=None, conn=None):

        if conn != None:
            self._conn = conn

        if not update:
            # reset ID
            if self._id and self._id.startswith("_"):
                self._id = None
            elif self._id:
                self._id = self._id.split(":").pop()

        lines = []

        # main command
        parts = []

        if not update:
            parts.append(indent + self._getControlName())
        
        # base props
        attrParts = self._get_cmd_attrs(update)

        if len(attrParts) > 0 or not update:
            parts.extend(attrParts)
            lines.append(" ".join(parts))

        if index != None:
            index.append(self)

        # controls
        for control in self._getChildren():
            childCmd = control.get_cmd_str(update=update, indent=indent+"  ", index=index)
            if childCmd != "":
                lines.append(childCmd)

        return "\n".join(lines)

    def _get_cmd_attrs(self, update=False):
        parts = []

        if update and not self._id:
            return parts

        for attrName in sorted(self._attrs):
            dirty = self._attrs[attrName][1]

            if update and not dirty:
                continue

            val = self._attrs[attrName][0]
            sval = ""
            if isinstance(val, bool):
                sval = str(val).lower()
            else:
                sval = encode_attr(val)

            parts.append(f'{attrName}="{sval}"')
            self._attrs[attrName] = (val, False)

        if self._id:
            if not update:
                parts.insert(0, f'id="{encode_attr(self._id)}"')
            elif len(parts) > 0:
                parts.insert(0, f'"{encode_attr(self._id)}"')
        
        return parts