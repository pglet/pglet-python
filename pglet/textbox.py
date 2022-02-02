from typing import Optional, Literal
from beartype import beartype
from pglet.control import Control

ALIGN = Literal[None, "left", "right", "center", "justify"]


class Textbox(Control):
    def __init__(
        self,
        label=None,
        id=None,
        value=None,
        placeholder=None,
        error_message=None,
        description=None,
        icon=None,
        icon_color=None,
        prefix=None,
        suffix=None,
        multiline=None,
        password=None,
        required=None,
        read_only=None,
        auto_adjust_height=None,
        underlined=None,
        borderless=None,
        on_change=None,
        width=None,
        height=None,
        padding=None,
        margin=None,
        align: ALIGN = None,
        visible=None,
        disabled=None,
    ):
        Control.__init__(
            self,
            id=id,
            width=width,
            height=height,
            padding=padding,
            margin=margin,
            visible=visible,
            disabled=disabled,
        )
        self.label = label
        self.value = value
        self.placeholder = placeholder
        self.error_message = error_message
        self.description = description
        self.icon = icon
        self.icon_color = icon_color
        self.suffix = suffix
        self.prefix = prefix
        self.align = align
        self.multiline = multiline
        self.read_only = read_only
        self.auto_adjust_height = auto_adjust_height
        self.underlined = underlined
        self.borderless = borderless
        self.password = password
        self.required = required
        self.on_change = on_change

    def _get_control_name(self):
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

    # prefix
    @property
    def prefix(self):
        return self._get_attr("prefix")

    @prefix.setter
    def prefix(self, value):
        self._set_attr("prefix", value)

    # suffix
    @property
    def suffix(self):
        return self._get_attr("suffix")

    @suffix.setter
    def suffix(self, value):
        self._set_attr("suffix", value)

    # align
    @property
    def align(self):
        return self._get_attr("align")

    @align.setter
    @beartype
    def align(self, value: ALIGN):
        self._set_attr("align", value)

    # multiline
    @property
    def multiline(self):
        return self._get_attr("multiline")

    @multiline.setter
    @beartype
    def multiline(self, value: Optional[bool]):
        self._set_attr("multiline", value)

    # read_only
    @property
    def read_only(self):
        return self._get_attr("readOnly")

    @read_only.setter
    @beartype
    def read_only(self, value: Optional[bool]):
        self._set_attr("readOnly", value)

    # auto_adjust_height
    @property
    def auto_adjust_height(self):
        return self._get_attr("autoadjustheight")

    @auto_adjust_height.setter
    @beartype
    def auto_adjust_height(self, value: Optional[bool]):
        self._set_attr("autoadjustheight", value)

    # underlined
    @property
    def underlined(self):
        return self._get_attr("underlined")

    @underlined.setter
    @beartype
    def underlined(self, value: Optional[bool]):
        self._set_attr("underlined", value)

    # borderless
    @property
    def borderless(self):
        return self._get_attr("borderless")

    @borderless.setter
    @beartype
    def borderless(self, value: Optional[bool]):
        self._set_attr("borderless", value)

    # password
    @property
    def password(self):
        return self._get_attr("password")

    @password.setter
    @beartype
    def password(self, value: Optional[bool]):
        self._set_attr("password", value)

    # required
    @property
    def required(self):
        return self._get_attr("required")

    @required.setter
    @beartype
    def required(self, value: Optional[bool]):
        self._set_attr("required", value)

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
            self._set_attr("onchange", None)
