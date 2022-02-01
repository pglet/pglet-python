from typing import Optional
from beartype import beartype
from pglet.control import Control


class Toggle(Control):
    def __init__(
        self,
        label=None,
        id=None,
        value=None,
        value_field=None,
        inline=None,
        on_text=None,
        off_text=None,
        data=None,
        on_change=None,
        width=None,
        height=None,
        padding=None,
        margin=None,
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
            data=data,
        )

        self.value = value
        self.value_field = value_field
        self.label = label
        self.inline = inline
        self.on_text = on_text
        self.off_text = off_text
        self.on_change = on_change

    def _get_control_name(self):
        return "toggle"

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
        return self._get_attr("value", data_type="bool")

    @value.setter
    @beartype
    def value(self, value: Optional[bool]):
        self._set_attr("value", value)

    # value_field
    @property
    def value_field(self):
        return self._get_attr("value")

    @value_field.setter
    def value_field(self, value):
        if value != None:
            self._set_attr("value", f"{{{value}}}")

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
    @beartype
    def inline(self, value: Optional[bool]):
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
