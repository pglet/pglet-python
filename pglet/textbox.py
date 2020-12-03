from .utils import encode_attr
from .control import Control

class Textbox(Control):
    def __init__(self, id=None, label=None, value=None, placeholder=None, errorMessage=None, description=None, multiline=False,
            visible=None, disabled=None):
        Control.__init__(self, id=id, visible=visible, disabled=disabled)
        self.label = label
        self.value = value
        self.placeholder = placeholder
        self.errorMessage = errorMessage
        self.description = description
        self.multiline = multiline

    def get_cmd_str(self, update=False, indent=''):
        parts = []

        if not update:
            parts.append(indent + "textbox")
        
        # base props
        parts.extend(Control._get_attrs_str(self, update))

        if self.label:
            parts.append(f"label=\"{encode_attr(self.label)}\"")

        if self.value:
            parts.append(f"value=\"{encode_attr(self.value)}\"")

        if self.placeholder:
            parts.append(f"placeholder=\"{encode_attr(self.placeholder)}\"")

        if self.errorMessage:
            parts.append(f"errorMessage=\"{encode_attr(self.errorMessage)}\"")

        if self.description:
            parts.append(f"description=\"{encode_attr(self.description)}\"")

        if self.multiline:
            parts.append(f"multiline=\"true\"")                        

        return " ".join(parts)