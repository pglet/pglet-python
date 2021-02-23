from .utils import encode_attr
from .control import Control

class Item(Control):
    def __init__(self, id=None, text=None, secondary_text=None, url=None, new_window=None, 
            icon=None, icon_color=None, icon_only=None, split=None, divider=None, onclick=None, items=[],
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
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
        self._items = []
        if items and len(items) > 0:
            for item in items:
                self.add_item(item)

    def _getControlName(self):
        return "item"

    def add_item(self, item):
        if isinstance(item, Item):
            self._items.append(item)
        else:
            self._items.append(Item(str(item)))

    # onclick
    @property
    def onclick(self):
        return None

    @onclick.setter
    def onclick(self, handler):
        self._add_event_handler("click", handler)

    # items
    @property
    def items(self):
        return self._items

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

    def _getChildren(self):
        return self._items

class Button(Control):
    def __init__(self, id=None, primary=None, compound=None, action=None, toolbar=None,
            split=None, text=None, secondary_text=None, url=None, new_window=None, 
            title=None, icon=None, icon_color=None, data=None, onclick=None, items=[],
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.primary = primary
        self.compound = compound
        self.action = action
        self.toolbar = toolbar
        self.split = split
        self.text = text
        self.secondary_text = secondary_text
        self.url = url
        self.new_window = new_window
        self.title = title
        self.icon = icon
        self.icon_color = icon_color
        self.data = data
        self.onclick = onclick
        self._items = []
        if items and len(items) > 0:
            for item in items:
                self.add_item(item)

    def _getControlName(self):
        return "button"
    
    def add_item(self, item):
        assert isinstance(item, Item), 'button can hold items only'
        self._items.append(item)

# onclick
    @property
    def onclick(self):
        return None

    @onclick.setter
    def onclick(self, handler):
        self._add_event_handler("click", handler)

# primary
    @property
    def primary(self):
        return self._get_attr("primary")

    @primary.setter
    def primary(self, value):
        assert value == None or isinstance(value, bool), "primary must be a boolean"
        self._set_attr("primary", value)

# compound
    @property
    def compound(self):
        return self._get_attr("compound")

    @compound.setter
    def compound(self, value):
        assert value == None or isinstance(value, bool), "compound must be a boolean"
        self._set_attr("compound", value)

# action
    @property
    def action(self):
        return self._get_attr("action")

    @action.setter
    def action(self, value):
        assert value == None or isinstance(value, bool), "action must be a boolean"
        self._set_attr("action", value)

# toolbar
    @property
    def toolbar(self):
        return self._get_attr("toolbar")

    @toolbar.setter
    def toolbar(self, value):
        assert value == None or isinstance(value, bool), "toolbar must be a boolean"
        self._set_attr("toolbar", value)

# split
    @property
    def split(self):
        return self._get_attr("split")

    @split.setter
    def split(self, value):
        assert value == None or isinstance(value, bool), "split must be a boolean"
        self._set_attr("split", value)

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
        assert value == None or isinstance(value, bool), "new_window must be a boolean"
        self._set_attr("newWindow", value)

# title
    @property
    def title(self):
        return self._get_attr("title")

    @title.setter
    def title(self, value):
        self._set_attr("title", value)

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

# data
    @property
    def data(self):
        return self._get_attr("data")

    @data.setter
    def data(self, value):
        self._set_attr("data", value)

    def _getChildren(self):
        return self._items