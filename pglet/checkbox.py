from .utils import encode_attr
from .control import Control

class Checkbox(Control):
    def __init__(self, label=None, id=None, value=None, value_field=None, box_side=None, data=None,
            width=None, height=None, padding=None, margin=None, onchange=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled, data=data)
        self.value = value
        self.value_field = value_field
        self.label = label
        self.box_side = box_side
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
        return self._get_attr("value", data_type="bool")

    @value.setter
    def value(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("value", value)

# value_field
    @property
    def value_field(self):
        return self._get_attr("value")

    @value_field.setter
    def value_field(self, value):
        if value != None:
            self._set_attr("value", f"{{{value}}}")

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