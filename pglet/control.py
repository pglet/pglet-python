from .utils import encode_attr

class Control:
    def __init__(self, id=None, visible=None, disabled=None):
        self._attrs = {}
        self._id = id
        self.visible = visible
        self.disabled = disabled

    def _getChildren(self):
        return []

    def _getControlName(self):
        raise Exception("_getControlName must be overridden in inherited class")

# id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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

    def get_cmd_str(self, update=False, indent='', index=None):
        lines = []

        # main command
        parts = []

        if not update:
            parts.append(indent + self._getControlName())
        
        # base props
        attrParts = self._get_attrs_str(update)

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

    def _get_attrs_str(self, update=False):
        parts = []

        if update and not self._id:
            return parts

        if not update:
            # reset ID
            if self._id and self._id.startswith("_"):
                self._id = None
            elif self._id:
                self._id = self._id.split(":").pop()

        for attrName in sorted(self._attrs):
            dirty = self._attrs[attrName][1]

            if not dirty:
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