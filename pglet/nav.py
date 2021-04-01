from .utils import encode_attr
from .control import Control

# Item
class Item(Control):
    def __init__(self, key=None, text=None, icon=None, icon_color=None, url=None, items=None,
        new_window=None, expanded=None):
        Control.__init__(self)
        #key and text are optional for group item but key or text are required for level 2 and deeper items 
        #assert key != None or text != None, "key or text must be specified"
        self.key = key
        self.text = text
        self.icon = icon
        self.icon_color = icon_color
        self.url = url
        self.new_window = new_window
        self.expanded = expanded
        self.__items = []
        if items != None:
            for item in items:
                self.__items.append(item)

    def _get_control_name(self):
        return "item"

    # items
    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

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

    # expanded
    @property
    def expanded(self):
        return self._get_attr("expanded", data_type="bool")

    @expanded.setter
    def expanded(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("expanded", value)

    def _get_children(self):
        return self.__items

class Nav(Control):
    def __init__(self, id=None, value=None, items=None,
            onchange=None, onexpand=None, oncollapse=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.value = value
        self.onchange = onchange
        self.onexpand = onexpand
        self.oncollapse = oncollapse
        self.__items = []
        if items != None:
            for item in items:
                self.__items.append(item)

    def _get_control_name(self):
        return "nav"

    # items
    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value
        
    # onchange
    @property
    def onchange(self):
        return self._get_event_handler("change")

    @onchange.setter
    def onchange(self, handler):
        self._add_event_handler("change", handler)

    # onexpand
    @property
    def onexpand(self):
        return self._get_event_handler("expand")

    @onexpand.setter
    def onexpand(self, handler):
        self._add_event_handler("expand", handler)

    # oncollapse
    @property
    def oncollapse(self):
        return self._get_event_handler("collapse")

    @oncollapse.setter
    def oncollapse(self, handler):
        self._add_event_handler("collapse", handler)

    # value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

    def _get_children(self):
        return self.__items
