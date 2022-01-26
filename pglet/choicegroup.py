from pglet.control import Control

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
    def __init__(self, label=None, id=None, value=None, data=None, options=None,
            width=None, height=None, padding=None, margin=None, on_change=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled, data=data)
        self.value = value
        self.label = label
        self.on_change = on_change
        self.__options = []
        if options != None:
            for option in options:
                self.__options.append(option)

    def _get_control_name(self):
        return "choicegroup"

    # options
    @property
    def options(self):
        return self.__options

    @options.setter
    def options(self, value):
        self.__options = value

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

    def _get_children(self):
        return self.__options
