from .utils import encode_attr
from .control import Control

class Slider(Control):
    def __init__(self, label=None, id=None, value=None, min=None, max=None, step=None,
            show_value=None, value_format=None, vertical=None, data=None, onchange=None,
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
        self.show_value = show_value
        self.value_format = value_format
        self.vertical = vertical
        self.data = data
        self.onchange = onchange

    def _get_control_name(self):
        return "slider"

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

# show_value
    @property
    def show_value(self):
        return self._get_attr("showValue")

    @show_value.setter
    def show_value(self, value):
        assert value == None or isinstance(value, bool), "show_value must be a boolean"
        self._set_attr("showValue", value)

# value_format
    @property
    def value_format(self):
        return self._get_attr("valueFormat")

    @value_format.setter
    def value_format(self, value):
        self._set_attr("valueFormat", value)

# vertical
    @property
    def vertical(self):
        return self._get_attr("vertical")

    @vertical.setter
    def vertical(self, value):
        assert value == None or isinstance(value, bool), "vertical must be a boolean"
        self._set_attr("vertical", value)

# data
    @property
    def data(self):
        return self._get_attr("data")

    @data.setter
    def data(self, value):
        self._set_attr("data", value)