from .utils import encode_attr
from .control import Control

# Option
class Option(Control):
    def __init__(self, key=None, text=None, icon=None, icon_color=None):
        Control.__init__(self)
        assert key != None or text != None, "key or text must be specified"

        self.key = key
        self.text = text
        self.icon = icon
        self.icon_color = icon_color

    def _get_control_name(self):
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

class ChoiceGroup(Control):
    def __init__(self, label=None, id=None, value=None, data=None, options=[],
            width=None, height=None, padding=None, margin=None, onchange=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        self.value = value
        self.label = label
        self.data = data
        self.onchange = onchange
        self._options = []
        if options and len(options) > 0:
            for option in options:
                self.add_option(option)

    def _get_control_name(self):
        return "choicegroup"

    def add_option(self, option):
        if isinstance(option, Option):
            self._options.append(option)
        else:
            self._options.append(Option(str(option)))

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
        self._set_attr("value", value)

    # label
    @property
    def label(self):
        return self._get_attr("label")

    @label.setter
    def label(self, value):
        self._set_attr("label", value)

    # data
    @property
    def data(self):
        return self._get_attr("data")

    @data.setter
    def data(self, value):
        self._set_attr("data", value)

    def _get_children(self):
        return self._options