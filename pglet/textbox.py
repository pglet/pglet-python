from .utils import encode_attr
from .control import Control

class Textbox(Control):
    def __init__(self, id=None, label=None, value=None, placeholder=None,
            error_message=None, description=None, multiline=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        self.label = label
        self.value = value
        self.placeholder = placeholder
        self.error_message = error_message
        self.description = description
        self.multiline = multiline

    def _getControlName(self):
        return "textbox"

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

# error_message
    @property
    def error_message(self):
        return self._get_attr("errorMessage")

    @error_message.setter
    def error_message(self, value):
        self._set_attr("errorMessage", value)

# description
    @property
    def description(self):
        return self._get_attr("description")

    @description.setter
    def description(self, value):
        self._set_attr("description", value)

# multiline
    @property
    def multiline(self):
        return self._get_attr("multiline")

    @multiline.setter
    def multiline(self, value):
        assert value == None or isinstance(value, bool), "multiline must be a boolean"
        self._set_attr("multiline", value)