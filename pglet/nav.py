from .utils import encode_attr
from .control import Control

# Item
class Item(Control):
    def __init__(self, key=None, text=None, icon=None, icon_color=None, url=None,
        new_window=None, expanded=None, collapsed=None):
        Control.__init__(self)
        assert key != None or text != None, "key or text must be specified"
        self.key = key
        self.text = text
        self.icon = icon
        self.icon_color = icon_color
        self.url = url
        self.new_window = new_window
        self.expanded = expanded
        self.collapsed = collapsed


    def _getControlName(self):
        return "item"

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
        return self._get_attr("expanded")

    @expanded.setter
    def expanded(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("expanded", value)

    # collapsed
    @property
    def collapsed(self):
        return self._get_attr("collapsed")

    @collapsed.setter
    def collapsed(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("collapsed", value)

class Nav(Control):
    def __init__(self, id=None, value=None, items=[],
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
        self._items = []
        if items and len(items) > 0:
            for item in items:
                self.add_item(item)

    def _getControlName(self):
        return "nav"

    def add_item(self, item):
        if isinstance(item, Item):
            self._items.append(item)
        else:
            self._items.append(Item(str(item)))

    # items
    @property
    def items(self):
        return self._items
        
    # onchange
    @property
    def onchange(self):
        return None

    @onchange.setter
    def onchange(self, handler):
        self._add_event_handler("change", handler)

    # onexpand
    @property
    def onexpand(self):
        return None

    @onexpand.setter
    def onexpand(self, handler):
        self._add_event_handler("expand", handler)

    # oncollapse
    @property
    def oncollapse(self):
        return None

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

    def _getChildren(self):
        return self._items