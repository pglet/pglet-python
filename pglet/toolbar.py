from typing import Optional
from beartype import beartype
from pglet.control import Control


class Toolbar(Control):
    def __init__(
        self,
        id=None,
        inverted=None,
        items=None,
        overflow=None,
        far=None,
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
        )

        self.__items = []
        if items != None:
            for item in items:
                self.__items.append(item)
        self.__overflow = Overflow(items=overflow)
        self.__far = Far(items=far)
        self.inverted = inverted

    def _get_control_name(self):
        return "toolbar"

    # inverted
    @property
    def inverted(self):
        return self._get_attr("inverted")

    @inverted.setter
    @beartype
    def inverted(self, value: Optional[bool]):
        self._set_attr("inverted", value)

    # items
    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

    # far
    @property
    def far_items(self):
        return self.__far.items

    @far_items.setter
    def far_items(self, value):
        self.__far.items = value

    # overflow
    @property
    def overflow_items(self):
        return self.__overflow.items

    @overflow_items.setter
    def overflow_items(self, value):
        self.__overflow.items = value

    def _get_children(self):
        result = []
        if self.__items and len(self.__items) > 0:
            for item in self.__items:
                result.append(item)
        result.append(self.__overflow)
        result.append(self.__far)
        return result


class Overflow(Control):
    def __init__(self, id=None, items=None):
        Control.__init__(self, id=id)

        self.__items = []
        if items != None:
            for item in items:
                self.__items.append(item)

    # items
    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

    def _get_control_name(self):
        return "overflow"

    def _get_children(self):
        return self.__items


class Far(Control):
    def __init__(self, id=None, items=None):
        Control.__init__(self, id=id)

        self.__items = []
        if items != None:
            for item in items:
                self.__items.append(item)

    # items
    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

    def _get_control_name(self):
        return "far"

    def _get_children(self):
        return self.__items


class Item(Control):
    def __init__(
        self,
        id=None,
        text=None,
        secondary_text=None,
        url=None,
        new_window=None,
        icon=None,
        icon_color=None,
        icon_only=None,
        split=None,
        divider=None,
        on_click=None,
        items=None,
        visible=None,
        disabled=None,
        data=None,
    ):
        Control.__init__(self, id=id, visible=visible, disabled=disabled, data=data)

        self.text = text
        self.secondary_text = secondary_text
        self.url = url
        self.new_window = new_window
        self.icon = icon
        self.icon_color = icon_color
        self.icon_only = icon_only
        self.split = split
        self.divider = divider
        self.on_click = on_click
        self.__items = []
        if items != None:
            for item in items:
                self.__items.append(item)

    def _get_control_name(self):
        return "item"

    # on_click
    @property
    def on_click(self):
        return self._get_event_handler("click")

    @on_click.setter
    def on_click(self, handler):
        self._add_event_handler("click", handler)

    # items
    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

    # text
    @property
    def text(self):
        return self._get_attr("text")

    @text.setter
    def text(self, value):
        self._set_attr("text", value)

    # secondary_text
    @property
    def secondary_text(self):
        return self._get_attr("secondaryText")

    @secondary_text.setter
    def secondary_text(self, value):
        self._set_attr("secondaryText", value)

    # url
    @property
    def url(self):
        return self._get_attr("url")

    @url.setter
    def url(self, value):
        self._set_attr("url", value)

    # new_window
    @property
    def new_window(self):
        return self._get_attr("newWindow")

    @new_window.setter
    @beartype
    def new_window(self, value: Optional[bool]):
        self._set_attr("newWindow", value)

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

    # icon_only
    @property
    def icon_only(self):
        return self._get_attr("iconOnly")

    @icon_only.setter
    @beartype
    def icon_only(self, value: Optional[bool]):
        self._set_attr("iconOnly", value)

    # split
    @property
    def split(self):
        return self._get_attr("split")

    @split.setter
    @beartype
    def split(self, value: Optional[bool]):
        self._set_attr("split", value)

    # divider
    @property
    def divider(self):
        return self._get_attr("divider")

    @divider.setter
    @beartype
    def divider(self, value: Optional[bool]):
        self._set_attr("divider", value)

    def _get_children(self):
        return self.__items
