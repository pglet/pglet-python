from .utils import encode_attr
from .control import Control

class Toggle(Control):
    def __init__(self, id=None, value=None, label=None, inline=None,
            on_text=None, off_text=None, data=None, onchange=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.value = value
        self.label = label
        self.inline = inline
        self.on_text = on_text
        self.off_text = off_text
        self.data = data
        self.onchange = onchange
       

    def _getControlName(self):
        return "toggle"

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
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("value", value)

# label
    @property
    def label(self):
        return self._get_attr("label")

    @label.setter
    def label(self, value):
        self._set_attr("label", value)

# inline
    @property
    def inline(self):
        return self._get_attr("inline")

    @inline.setter
    def inline(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("inline", value)

# on_text
    @property
    def on_text(self):
        return self._get_attr("onText")

    @on_text.setter
    def on_text(self, value):
        self._set_attr("onText", value)

# off_text
    @property
    def off_text(self):
        return self._get_attr("offText")

    @off_text.setter
    def off_text(self, value):
        self._set_attr("offText", value)

# data
    @property
    def data(self):
        return self._get_attr("data")

    @data.setter
    def data(self, value):
        self._set_attr("data", value)

