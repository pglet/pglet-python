from datetime import datetime, date
from .control import Control

class DatePicker(Control):
    def __init__(self, label=None, id=None, value=None, placeholder=None,
            required=None, allow_text_input=None, underlined=None, borderless=None,
            on_change=None,
            width=None, visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width,
            visible=visible, disabled=disabled)
        self.label = label
        self.value = value
        self.placeholder = placeholder
        self.allow_text_input = allow_text_input
        self.underlined = underlined
        self.borderless = borderless
        self.required = required
        self.on_change = on_change

    def _get_control_name(self):
        return "datepicker"

    def _set_attr(self, name, value, dirty=True):
        d = value
        if d == "":
            d = None
        elif name == "value" and d != None and not isinstance(d, date):
            d = datetime.fromisoformat(value.replace('Z', '+00:00'))
        self._set_attr_internal(name, d, dirty)

# label
    @property
    def label(self):
        return self._get_attr("label")

    @label.setter
    def label(self, value):
        self._set_attr("label", value)

# value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

# placeholder
    @property
    def placeholder(self):
        return self._get_attr("placeholder")

    @placeholder.setter
    def placeholder(self, value):
        self._set_attr("placeholder", value)

# allow_text_input
    @property
    def allow_text_input(self):
        return self._get_attr("allowTextInput")

    @allow_text_input.setter
    def allow_text_input(self, value):
        assert value == None or isinstance(value, bool), "allow_text_input must be a boolean"
        self._set_attr("allowTextInput", value)

# underlined
    @property
    def underlined(self):
        return self._get_attr("underlined")

    @underlined.setter
    def underlined(self, value):
        assert value == None or isinstance(value, bool), "underlined must be a boolean"
        self._set_attr("underlined", value)

# borderless
    @property
    def borderless(self):
        return self._get_attr("borderless")

    @borderless.setter
    def borderless(self, value):
        assert value == None or isinstance(value, bool), "borderless must be a boolean"
        self._set_attr("borderless", value)                                

# required
    @property
    def required(self):
        return self._get_attr("required")

    @required.setter
    def required(self, value):
        assert value == None or isinstance(value, bool), "required must be a boolean"
        self._set_attr("required", value)

# on_change
    @property
    def on_change(self):
        return self._get_event_handler("change")

    @on_change.setter
    def on_change(self, handler):
        self._add_event_handler("change", handler)