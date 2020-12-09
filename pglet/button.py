from .utils import encode_attr
from .control import Control

class Button(Control):
    def __init__(self, id=None, text=None, primary=None, data=None, onclick=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        self.text = text
        self.primary = primary
        self.data = data
        self.onclick = onclick

    def _getControlName(self):
        return "button"

# text
    @property
    def onclick(self):
        return None

    @onclick.setter
    def onclick(self, handler):
        self._add_event_handler("click", handler)

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