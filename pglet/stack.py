from .utils import encode_attr
from .control import Control
from .alignment import Alignment

class Stack(Control):

    def __init__(self, id=None, horizontal=False, horizontalAlign=None,
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

    def get_cmd_str(self, update=False, indent=''):
        lines = []

        # main command
        parts = []

        if not update:
            parts.append(indent + "stack")
        
        # base props
        parts.extend(Control._get_attrs_str(self, update))

        if self.horizontal != None:
            parts.append(f'horizontal="{encode_attr(self.horizontal)}"')

        if self.horizontalAlign != None:
            parts.append(f'horizontalAlign="{self.horizontalAlign}"')

        if self.verticalAlign:
            parts.append(f'verticalAlign="{self.verticalAlign}"')

        lines.append(" ".join(parts))

        # # options
        # if not update:
        #     for option in self.options:
        #         parts.clear()
        #         parts.append(indent + "  option")

        #         if option.key:
        #             parts.append(f"key=\"{encode_attr(option.key)}\"")

        #         if option.text:
        #             parts.append(f"text=\"{encode_attr(option.text)}\"")

        #         lines.append(" ".join(parts))

        return "\n".join(lines)