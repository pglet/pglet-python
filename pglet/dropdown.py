from .utils import encode_attr
from .control import Control

# Option
class Option(Control):
    def __init__(self, key=None, text=None):
        Control.__init__(self)
        assert key != None or text != None, "key or text must be specified"
        self.key = key
        self.text = text

    def _getControlName(self):
        return "option"

    # key
    @property
    def key(self):
        return self._get_attr("key")

    @key.setter
    def key(self, value):
        self._set_attr("key", value)

    # text
    @property
    def text(self):
        return self._get_attr("text")

    @text.setter
    def text(self, value):
        self._set_attr("text", value)

class Dropdown(Control):
    def __init__(self, label=None, id=None, value=None, placeholder=None,
            error_message=None, onchange=None, options=[],
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        self.label = label
        self.value = value
        self.placeholder = placeholder
        self.error_message = error_message
        self.onchange = onchange
        self._options = []
        if options and len(options) > 0:
            for option in options:
                self.add_option(option)

    def _getControlName(self):
        return "dropdown"

    def add_option(self, option):
        if isinstance(option, Option):
            self._options.append(option)
        else:
            self._options.append(Option(str(option)))

    # options
    @property
    def options(self):
        return self._options
        
    # onchange
    @property
    def onchange(self):
        return None

    @onchange.setter
    def onchange(self, handler):
        self._add_event_handler("change", handler)

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

    def _getChildren(self):
        return self._options