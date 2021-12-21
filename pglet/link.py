from .control import Control

class Link(Control):
    def __init__(self, url=None, id=None, value=None, new_window=None, title=None,
            size=None, bold=None, italic=None, pre=None, align=None, on_click=None, controls=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None, data=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled, data=data)
        
        self.value = value
        self.url = url
        self.new_window = new_window
        self.title = title
        self.size = size
        self.bold = bold
        self.italic = italic
        self.pre = pre
        self.align = align
        self.on_click = on_click
        self.__controls = []
        if controls != None:
            for control in controls:
                self.__controls.append(control)

    def _get_control_name(self):
        return "link"

# controls
    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value):
        self.__controls = value

# on_click
    @property
    def on_click(self):
        return self._get_event_handler("click")

    @on_click.setter
    def on_click(self, handler):
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
        

    def _get_children(self):
        return self.__controls
