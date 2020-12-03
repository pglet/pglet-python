from .utils import encode_attr
from .control import Control

class Text(Control):
    def __init__(self, id=None, value=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id, visible=visible, disabled=disabled)
        self.value = value

    def get_cmd_str(self, update=False, indent='', index=None):
        parts = []

        if not update:
            parts.append(indent + "text")
        
        # base props
        parts.extend(Control._get_attrs_str(self, update))

        if self.value:
            parts.append(f"value=\"{encode_attr(self.value)}\"")

        if index != None:
            index.append(self)

        return " ".join(parts)