from .utils import encode_attr
from .control import Control

class Button(Control):
    def __init__(self, id=None, text=None, data=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id, visible=visible, disabled=disabled)
        self.text = text
        self.data = data

    def get_cmd_str(self, update=False, indent='', index=None):
        parts = []

        if not update:
            parts.append(indent + "button")
        
        # base props
        parts.extend(Control._get_attrs_str(self, update))

        if self.text:
            parts.append(f"text=\"{encode_attr(self.text)}\"")

        if self.data:
            parts.append(f"data=\"{encode_attr(self.data)}\"")

        if index != None:
            index.append(self)

        return " ".join(parts)