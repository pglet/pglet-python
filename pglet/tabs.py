from .utils import encode_attr
from .control import Control

# Tab
class Tab(Control):
    def __init__(self, text, controls=[], id=None, key=None, icon=None, count=None):
        Control.__init__(self, id=id)
        #key or text are required 
        assert key != None or text != None, "key or text must be specified"
        self.key = key
        self.text = text
        self.icon = icon
        self.count = count
        self._controls = []
        if controls and len(controls) > 0:
            for control in controls:
                self.add_control(control)

    def _getControlName(self):
        return "tab"

    def add_control(self, control):
        if not isinstance(control, Control):
            raise Exception("Stack can hold controls only")
        self._controls.append(control)

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

    # count
    @property
    def count(self):
        return self._get_attr("count")

    @count.setter
    def count(self, value):
        self._set_attr("count", value)

    def _getChildren(self):
        return self._controls

class Tabs(Control):
    def __init__(self, tabs=[], id=None, value=None, solid=None,
            onchange=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.value = value
        self.solid = solid
        self.onchange = onchange
        self._tabs = []
        if tabs and len(tabs) > 0:
            for tab in tabs:
                self.add_tab(tab)

    def _getControlName(self):
        return "tabs"

    def add_tab(self, tab):
        assert isinstance(tab, Tab), 'tabs can hold tab only'
        self._tabs.append(tab)

    # tabs
    @property
    def tabs(self):
        return self._tabs
        
    # onchange
    @property
    def onchange(self):
        return None

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

    # solid
    @property
    def solid(self):
        return self._get_attr("solid")

    @solid.setter
    def solid(self, value):
        assert value == None or isinstance(value, bool), "show_value must be a boolean"
        self._set_attr("solid", value)

    def _getChildren(self):
        return self._tabs