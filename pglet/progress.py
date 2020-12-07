from .utils import encode_attr
from .control import Control

class Progress(Control):
    def __init__(self, id=None, label=None, description=None, value=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        self.value = value
        self.description = description
        self.label = label

    def _getControlName(self):
        return "progress"

# value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        assert value == None or isinstance(value, int), "value must be an int"
        self._set_attr("value", value)

# description
    @property
    def description(self):
        return self._get_attr("description")

    @description.setter
    def description(self, value):
        self._set_attr("description", value)

# label
    @property
    def label(self):
        return self._get_attr("label")

    @label.setter
    def label(self, value):
        self._set_attr("label", value)