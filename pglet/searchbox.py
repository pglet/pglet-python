from .utils import encode_attr
from .control import Control

class SearchBox(Control):
    def __init__(self, id=None, value=None, placeholder=None, underlined=None,
            icon=None, icon_color=None, data=None, on_search=None,
            on_clear=None, on_escape=None, on_change=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):

        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled, data=data)

        self.value = value
        self.placeholder = placeholder
        self.underlined = underlined
        self.icon = icon
        self.icon_color = icon_color
        self.on_search = on_search
        self.on_clear = on_clear
        self.on_escape = on_escape
        self.on_change = on_change

    def _get_control_name(self):
        return "searchbox"

# on_search
    @property
    def on_search(self):
        return self._get_event_handler("search")

    @on_search.setter
    def on_search(self, handler):
        self._add_event_handler("search", handler)

# on_clear
    @property
    def on_clear(self):
        return self._get_event_handler("clear")

    @on_clear.setter
    def on_clear(self, handler):
        self._add_event_handler("clear", handler)

# on_escape
    @property
    def on_escape(self):
        return self._get_event_handler("escape")

    @on_escape.setter
    def on_escape(self, handler):
        self._add_event_handler("escape", handler)

# on_change
    @property
    def on_change(self):
        return self._get_event_handler("change")

    @on_change.setter
    def on_change(self, handler):
        self._add_event_handler("change", handler)
        if handler != None:
            self._set_attr("onchange", True)
        else:
            self._set_attr("onchange", False)

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

# underlined
    @property
    def underlined(self):
        return self._get_attr("underlined")

    @underlined.setter
    def underlined(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("underlined", value)

# icon
    @property
    def icon(self):
        return self._get_attr("icon")

    @icon.setter
    def icon(self, value):
        self._set_attr("icon", value)

# icon_color
    @property
    def icon_color(self):
        return self._get_attr("iconColor")

    @icon_color.setter
    def icon_color(self, value):
        self._set_attr("iconColor", value)