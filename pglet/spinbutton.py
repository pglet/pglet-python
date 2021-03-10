from .utils import encode_attr
from .control import Control

class SpinButton(Control):
    def __init__(self, label=None, id=None, value=None, min=None, max=None, step=None,
            icon=None, data=None, onchange=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        self.value = value
        self.label = label
        self.min = min
        self.max = max
        self.step = step
        self.icon = icon
        self.data = data
        self.onchange = onchange

    def _getControlName(self):
        return "spinbutton"

# onchange
    @property
    def onchange(self):
        return None

    @onchange.setter
    def onchange(self, handler):
        self._add_event_handler("change", handler)

# value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        assert value == None or isinstance(value, float) or isinstance(value, int), "value must be a float"
        self._set_attr("value", float(value))

# label
    @property
    def label(self):
        return self._get_attr("label")

    @label.setter
    def label(self, value):
        self._set_attr("label", value)

# min
    @property
    def min(self):
        return self._get_attr("min")

    @min.setter
    def min(self, value):
        assert value == None or isinstance(value, float) or isinstance(value, int), "min must be a float"
        self._set_attr("min", float(value))

# max
    @property
    def max(self):
        return self._get_attr("max")

    @max.setter
    def max(self, value):
        assert value == None or isinstance(value, float) or isinstance(value, int), "max must be a float"
        self._set_attr("max", float(value))

# step
    @property
    def step(self):
        return self._get_attr("step")

    @step.setter
    def step(self, value):
        assert value == None or isinstance(value, float) or isinstance(value, int), "step must be a float"
        self._set_attr("step", float(value))

# icon
    @property
    def icon(self):
        return self._get_attr("icon")

    @icon.setter
    def icon(self, value):
        self._set_attr("icon", value)

# data
    @property
    def data(self):
        return self._get_attr("data")

    @data.setter
    def data(self, value):
        self._set_attr("data", value)