from .utils import encode_attr
from .control import Control

# Item
class Item(Control):
    def __init__(self, text=None, secondary_text=None, url=None, new_window=None,
    icon=None, icon_color=None, icon_only=None, split=None, divider=None,
    onclick=None, items=[]):
        Control.__init__(self)

        self.text = text
        self.secondary_text = secondary_text
        self.url = url
        self.new_window = new_window
        self.icon = icon
        self.icon_color = icon_color
        self.icon_only = icon_only
        self.split = split
        self.divider = divider
        self.onclick = onclick
        self._items = items

    def _get_control_name(self):
        return "item"

    # onclick
    @property
    def onclick(self):
        return self._get_event_handler("click")

    @onclick.setter
    def onclick(self, handler):
        self._add_event_handler("click", handler)

    # items
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

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
    def new_window(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
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
    def icon_only(self, value):
        assert value == None or isinstance(value, bool), "icon_only must be a boolean"
        self._set_attr("iconOnly", value)

    # split
    @property
    def split(self):
        return self._get_attr("split")

    @split.setter
    def split(self, value):
        assert value == None or isinstance(value, bool), "split must be a boolean"
        self._set_attr("split", value)

    # divider
    @property
    def divider(self):
        return self._get_attr("divider")

    @divider.setter
    def divider(self, value):
        assert value == None or isinstance(value, bool), "divider must be a boolean"
        self._set_attr("divider", value)

    def _get_children(self):
        return self._items

# Overflow
class Overflow(Control):
    def __init__(self, id=None, items=[]):
        Control.__init__(self, id=id)
    
        self._items = items

    # items
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    def _get_control_name(self):
        return "overflow"

    def _get_children(self):
        return self._items

# Far
class Far(Control):
    def __init__(self, id=None, items=[]):
        Control.__init__(self, id=id)
    
        self._items = items

    # items
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    def _get_control_name(self):
        return "far"

    def _get_children(self):
        return self._items



class Toolbar(Control):
    def __init__(self, id=None, inverted=None, items=[], overflow=[], far=[],
            width=None, height=None, padding=None, margin=None, visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)

        self._items = items
        self._overflow = Overflow(items=overflow)
        self._far = Far(items=far)
        self.inverted = inverted
        
    def _get_control_name(self):
        return "toolbar"

    # inverted
    @property
    def inverted(self):
        return self._get_attr("inverted")

    @inverted.setter
    def inverted(self, value):
        assert value == None or isinstance(value, bool), "inverted must be a boolean"
        self._set_attr("inverted", value)

    # items
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    # far
    @property
    def far_items(self):
        return self._far.items

    @far_items.setter
    def far_items(self, value):
        self._far.items = value

    # overflow
    @property
    def overflow_items(self):
        return self._overflow.items

    @overflow_items.setter
    def overflow_items(self, value):
        self._overflow.items = value

    def _get_children(self):
        result=[]
        if self._items and len(self._items) > 0:
            for item in self._items:
                result.append(item)
        result.append(self._overflow)
        result.append(self._far)
        return result