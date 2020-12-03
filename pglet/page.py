from .utils import encode_attr
from .control import Control
from .alignment import Alignment

class Page(Control):

    def __init__(self, id=None, verticalFill=None, horizontalAlign=None,
            verticalAlign=None, width=None, padding=None):
        Control.__init__(self, id="page")

        self.verticalFill = verticalFill

        if horizontalAlign != None and not isinstance(horizontalAlign, Alignment):
            raise Exception("horizontalAlign must be of Alignment type")
        self.horizontalAlign = horizontalAlign

        if verticalAlign != None and not isinstance(verticalAlign, Alignment):
            raise Exception("verticalAlign must be of Alignment type")

        self.verticalAlign = verticalAlign
        self.width = width
        self.padding = padding

    def get_cmd_str(self, update=False, indent='', index=None):

        if not update:
            raise Exception("Page control cannot be added, only updated.")

        parts = []
        
        # base props
        parts.extend(Control._get_attrs_str(self, update))

        if self.verticalFill != None:
            parts.append(f'verticalFill="{str(self.verticalFill).lower()}"')

        if self.horizontalAlign != None:
            parts.append(f'horizontalAlign="{self.horizontalAlign}"')

        if self.verticalAlign != None:
            parts.append(f'verticalAlign="{self.verticalAlign}"')

        if self.width != None:
            parts.append(f'width="{self.width}"')

        if self.padding != None:
            parts.append(f'padding="{self.padding}"')

        return " ".join(parts)