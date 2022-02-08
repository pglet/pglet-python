from typing import List, Literal, Optional

from beartype import beartype

from pglet.control import Control

ITEM_TYPE = Literal[None, "normal", "divider", "header", "selectAll", "select_all"]


class ComboBox(Control):
    def __init__(
        self,
        label=None,
        id=None,
        value=None,
        placeholder=None,
        error_message=None,
        on_change=None,
        on_focus=None,
        on_blur=None,
        options=None,
        width=None,
        height=None,
        padding=None,
        margin=None,
        visible=None,
        disabled=None,
        focused=None,
        multi_select=None,
        allow_free_form=None,
        auto_complete=None,
        data=None,
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
        self.label = label
        self.value = value
        self.placeholder = placeholder
        self.error_message = error_message
        self.focused = focused
        self.multi_select = multi_select
        self.allow_free_form = allow_free_form
        self.auto_complete = auto_complete
        self.on_change = on_change
        self.on_focus = on_focus
        self.on_blur = on_blur
        self.__options = []
        if options != None:
            for option in options:
                self.__options.append(option)

    def _get_control_name(self):
        return "combobox"

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
        v = self._get_attr("value")
        if v and self.multi_select:
            return [x.strip() for x in v.split(",")]
        return v

    @value.setter
    def value(self, value):
        if isinstance(value, List):
            value = ",".join(value)
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

    def _get_children(self):
        return self.__options

    # focused
    @property
    def focused(self):
        return self._get_attr("focused")

    @focused.setter
    @beartype
    def focused(self, value: Optional[bool]):
        self._set_attr("focused", value)

    # multi_select
    @property
    def multi_select(self):
        return self._get_attr("multiselect")

    @multi_select.setter
    @beartype
    def multi_select(self, value: Optional[bool]):
        self._set_attr("multiselect", value)

    # allow_free_form
    @property
    def allow_free_form(self):
        return self._get_attr("allowfreeform")

    @allow_free_form.setter
    @beartype
    def allow_free_form(self, value: Optional[bool]):
        self._set_attr("allowfreeform", value)

    # auto_complete
    @property
    def auto_complete(self):
        return self._get_attr("autocomplete")

    @auto_complete.setter
    @beartype
    def auto_complete(self, value: Optional[bool]):
        self._set_attr("autocomplete", value)

    # on_focus
    @property
    def on_focus(self):
        return self._get_event_handler("focus")

    @on_focus.setter
    def on_focus(self, handler):
        self._add_event_handler("focus", handler)

    # on_blur
    @property
    def on_blur(self):
        return self._get_event_handler("blur")

    @on_blur.setter
    def on_blur(self, handler):
        self._add_event_handler("blur", handler)


class Option(Control):
    def __init__(self, key=None, text=None, item_type: ITEM_TYPE = None, disabled=None):
        Control.__init__(self)
        assert key != None or text != None, "key or text must be specified"
        self.key = key
        self.text = text
        self.item_type = item_type
        self.disabled = disabled

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

    # item_type
    @property
    def item_type(self):
        return self._get_attr("itemtype")

    @item_type.setter
    @beartype
    def item_type(self, value: ITEM_TYPE):
        self._set_attr("itemtype", value)

    # disabled
    @property
    def disabled(self):
        return self._get_attr("disabled")

    @disabled.setter
    @beartype
    def disabled(self, value: Optional[bool]):
        self._set_attr("disabled", value)
