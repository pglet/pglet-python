from .utils import encode_attr
from .control import Control

class Text(Control):
    def __init__(self, id=None, value=None, align=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):

        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)

        self.value = value
        self.align = align

    def _getControlName(self):
        return "text"

# value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

# align
    @property
    def align(self):
        return self._get_attr("align")

    @align.setter
    def align(self, value):
        self._set_attr("align", value)
