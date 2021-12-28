from .control import Control

class SpinButton(Control):
    def __init__(self, label=None, id=None, value=None, min=None, max=None, step=None,
            icon=None, label_position=None, data=None, on_change=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled, data=data)
        self.value = value
        self.label = label
        self.label_position = label_position
        self.min = min
        self.max = max
        self.step = step
        self.icon = icon
        self.on_change = on_change

    def _get_control_name(self):
        return "spinbutton"

# on_change
    @property
    def on_change(self):
        return self._get_event_handler("change")

    @on_change.setter
    def on_change(self, handler):
        self._add_event_handler("change", handler)

# value
    @property
    def value(self):
        return self._get_attr("value", data_type="float")

    @value.setter
    def value(self, value):
        assert value == None or isinstance(value, float) or isinstance(value, int), "value must be a float"
        self._set_attr("value", value)

# label
    @property
    def label(self):
        return self._get_attr("label")

    @label.setter
    def label(self, value):
        self._set_attr("label", value)

# label_position
    @property
    def label_position(self):
        return self._get_attr("labelposition")

    @label_position.setter
    def label_position(self, value):
        self._set_attr("labelposition", value)        

# min
    @property
    def min(self):
        return self._get_attr("min")

    @min.setter
    def min(self, value):
        assert value == None or isinstance(value, float) or isinstance(value, int), "min must be a float"
        self._set_attr("min", value)

# max
    @property
    def max(self):
        return self._get_attr("max")

    @max.setter
    def max(self, value):
        assert value == None or isinstance(value, float) or isinstance(value, int), "max must be a float"
        self._set_attr("max", value)

# step
    @property
    def step(self):
        return self._get_attr("step")

    @step.setter
    def step(self, value):
        assert value == None or isinstance(value, float) or isinstance(value, int), "step must be a float"
        self._set_attr("step", value)

# icon
    @property
    def icon(self):
        return self._get_attr("icon")

    @icon.setter
    def icon(self, value):
        self._set_attr("icon", value)