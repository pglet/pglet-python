from .utils import encode_attr
from .control import Control

class Checkbox(Control):
    def __init__(self, label=None, id=None, value=None, box_side=None, data=None,
            width=None, height=None, padding=None, margin=None, onchange=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        self.value = value
        self.label = label
        self.box_side = box_side
        self.data = data
        self.onchange = onchange

    def _get_control_name(self):
        return "checkbox"

# onchange
    @property
    def onchange(self):
        return self._get_event_handler("change")

    @onchange.setter
    def onchange(self, handler):
        self._add_event_handler("change", handler)

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

# box_side
    @property
    def box_side(self):
        return self._get_attr("boxSide")

    @box_side.setter
    def box_side(self, value):
        self._set_attr("boxSide", value)

# data
    @property
    def data(self):
        return self._get_attr("data")

    @data.setter
    def data(self, value):
        self._set_attr("data", value)