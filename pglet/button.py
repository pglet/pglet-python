from .utils import encode_attr
from .control import Control

class Button(Control):
    def __init__(self, id=None, text=None, primary=None, data=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id, visible=visible, disabled=disabled)
        self.text = text
        self.primary = primary
        self.data = data

    def _getControlName(self):
        return "button"

# text
    @property
    def text(self):
        return self._get_attr("text")

    @text.setter
    def text(self, value):
        self._set_attr("text", value)

# primary
    @property
    def primary(self):
        return self._get_attr("primary")

    @primary.setter
    def primary(self, value):
        assert value == None or isinstance(value, bool), "primary must be a boolean"
        self._set_attr("primary", value)

# data
    @property
    def data(self):
        return self._get_attr("data")

    @data.setter
    def data(self, value):
        self._set_attr("data", value)