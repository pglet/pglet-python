from pglet.control import Control

# Tab
class Tab(Control):
    def __init__(self, text, controls=None, id=None, key=None, icon=None, count=None):
        Control.__init__(self, id=id)
        #key or text are required 
        assert key != None or text != None, "key or text must be specified"
        self.key = key
        self.text = text
        self.icon = icon
        self.count = count
        self.__controls = []
        if controls != None:
            for control in controls:
                self.__controls.append(control)        

    def _get_control_name(self):
        return "tab"

    # controls
    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value):
        self.__controls = value        

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

    def _get_children(self):
        return self.__controls

class Tabs(Control):
    def __init__(self, tabs=None, id=None, value=None, solid=None,
            on_change=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.value = value
        self.solid = solid
        self.on_change = on_change
        self.__tabs = []
        if tabs != None:
            for tab in tabs:
                self.__tabs.append(tab)                

    def _get_control_name(self):
        return "tabs"

    def clean(self):
        Control.clean(self)
        self.__tabs.clear()

    # tabs
    @property
    def tabs(self):
        return self.__tabs

    @tabs.setter
    def tabs(self, value):
        self.__tabs = value
        
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

    # solid
    @property
    def solid(self):
        return self._get_attr("solid")

    @solid.setter
    def solid(self, value):
        assert value == None or isinstance(value, bool), "show_value must be a boolean"
        self._set_attr("solid", value)

    def _get_children(self):
        return self.__tabs
