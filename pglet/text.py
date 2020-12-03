from .utils import encode_attr
from .control import Control

class Text(Control):
    def __init__(self, id=None, value=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id, visible=visible, disabled=disabled)
        self.value = value

    def _getControlName(self):
        return "text"

# value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)