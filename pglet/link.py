from .utils import encode_attr
from .control import Control

class Link(Control):
    def __init__(self, id=None, value=None, url=None, new_window=None, title=None,
            size=None, bold=None, italic=None, pre=None, align=None, onclick=None, controls=[],
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.value = value
        self.url = url
        self.new_window = new_window
        self.title = title
        self.size = size
        self.bold = bold
        self.italic = italic
        self.pre = pre
        self.align = align
        self.onclick = onclick
        self._controls = []
        if controls and len(controls) > 0:
            for control in controls:
                self.add_control(control)

    def _getControlName(self):
        return "link"

    def add_control(self, control):
        assert isinstance(control, Control), 'link can hold controls only'
        self._controls.append(control)

# controls
    @property
    def controls(self):
        return self._controls

# onclick
    @property
    def onclick(self):
        return None

    @onclick.setter
    def onclick(self, handler):
        self._add_event_handler("click", handler)

# value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

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

# title
    @property
    def title(self):
        return self._get_attr("title")

    @title.setter
    def title(self, value):
        self._set_attr("title", value)

# size
    @property
    def size(self):
        return self._get_attr("size")

    @size.setter
    def size(self, value):
        self._set_attr("size", value)

# bold
    @property
    def bold(self):
        return self._get_attr("bold")

    @bold.setter
    def bold(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("bold", value)

# italic
    @property
    def italic(self):
        return self._get_attr("italic")

    @italic.setter
    def italic(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("italic", value)

# pre
    @property
    def pre(self):
        return self._get_attr("pre")

    @pre.setter
    def pre(self, value):
        assert value == None or isinstance(value, bool), "pre must be a boolean"
        self._set_attr("pre", value)

# align
    @property
    def align(self):
        return self._get_attr("align")

    @align.setter
    def align(self, value):
        self._set_attr("align", value)
        

    def _getChildren(self):
        result=[]
        if self._controls and len(self._controls) > 0:
            for control in self._controls:
                result.append(control)
        return result