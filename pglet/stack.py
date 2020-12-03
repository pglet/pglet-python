from .utils import encode_attr
from .control import Control
from .alignment import Alignment

class Stack(Control):

    def __init__(self, id=None, horizontal=None, horizontalAlign=None,
            verticalAlign=None, width=None, controls=[],
            visible=None, disabled=None):
        Control.__init__(self, id=id, visible=visible, disabled=disabled)

        self.horizontal = horizontal

        if horizontalAlign != None and not isinstance(horizontalAlign, Alignment):
            raise Exception("horizontalAlign must be of Alignment type")
        self.horizontalAlign = horizontalAlign

        if verticalAlign != None and not isinstance(verticalAlign, Alignment):
            raise Exception("verticalAlign must be of Alignment type")

        self.verticalAlign = verticalAlign
        self.width = width
        self.controls = []
        if controls and len(controls) > 0:
            for control in controls:
                self.add_control(control)

    def add_control(self, control):
        if not isinstance(control, Control):
            raise Exception("Stack can hold controls only")

        self.controls.append(control)

    def get_cmd_str(self, update=False, indent='', index=None):
        lines = []

        # main command
        parts = []

        if not update:
            parts.append(indent + "stack")
        
        # base props
        parts.extend(Control._get_attrs_str(self, update))

        if self.horizontal != None:
            parts.append(f'horizontal="{str(self.horizontal).lower()}"')

        if self.horizontalAlign != None:
            parts.append(f'horizontalAlign="{self.horizontalAlign}"')

        if self.verticalAlign != None:
            parts.append(f'verticalAlign="{self.verticalAlign}"')

        lines.append(" ".join(parts))

        if index != None:
            index.append(self)

        # controls
        if not update:
            for control in self.controls:
                lines.append(control.get_cmd_str(update=update, indent=indent+"  ", index=index))

        return "\n".join(lines)