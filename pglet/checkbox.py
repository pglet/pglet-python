from .utils import encode_attr
from .control import Control

class Checkbox(Control):
    def __init__(self, id=None, label=None, value=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id, visible=visible, disabled=disabled)
        self.value = value
        self.label = label

    def get_cmd_str(self, update=False, indent='', index=None):
        parts = []

        if not update:
            parts.append(indent + "checkbox")
        
        # base props
        parts.extend(Control._get_attrs_str(self, update))

        if self.label != None:
            parts.append(f'label="{encode_attr(self.label)}"')

        if self.value != None:
            parts.append(f'value="{str(self.value).lower()}"')

        if index != None:
            index.append(self)

        return " ".join(parts)