from .utils import encode_attr
from .control import Control

class Text(Control):
    def __init__(self, id=None, value=None, align=None, verticalAlign=None,
            size=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):

        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)

        self.value = value
        self.align = align
        self.verticalAlign = verticalAlign
        self.size = size

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

# verticalAlign
    @property
    def verticalAlign(self):
        return self._get_attr("verticalAlign")

    @verticalAlign.setter
    def verticalAlign(self, value):
        self._set_attr("verticalAlign", value)

# size
    @property
    def size(self):
        return self._get_attr("size")

    @size.setter
    def size(self, value):
        self._set_attr("size", value)