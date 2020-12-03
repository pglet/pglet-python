from .utils import encode_attr
from .control import Control

class Checkbox(Control):
    def __init__(self, id=None, label=None, value=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id, visible=visible, disabled=disabled)
        self.value = value
        self.label = label

    def _getControlName(self):
        return "checkbox"

# value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("value", value)

# label
    @property
    def label(self):
        return self._get_attr("label")

    @label.setter
    def label(self, value):
        self._set_attr("label", value)