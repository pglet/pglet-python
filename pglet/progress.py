from .utils import encode_attr
from .control import Control

class Progress(Control):
    def __init__(self, id=None, label=None, description=None, value=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id, visible=visible, disabled=disabled)
        self.value = value
        self.description = description
        self.label = label

    def get_cmd_str(self, update=False, indent='', index=None):
        parts = []

        if not update:
            parts.append(indent + "progress")
        
        # base props
        parts.extend(Control._get_attrs_str(self, update))

        if self.label:
            parts.append(f"label=\"{encode_attr(self.label)}\"")

        if self.value:
            parts.append(f"value=\"{encode_attr(self.value)}\"")

        if self.description:
            parts.append(f"description=\"{encode_attr(self.description)}\"")

        if index != None:
            index.append(self)

        return " ".join(parts)