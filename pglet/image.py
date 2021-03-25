from .utils import encode_attr
from .control import Control

class Image(Control):
    def __init__(self, src=None, id=None, alt=None, title=None, maximize_frame=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.src = src
        self.alt = alt
        self.title = title
        self.maximize_frame = maximize_frame

    def _get_control_name(self):
        return "image"

# src
    @property
    def src(self):
        return self._get_attr("src")

    @src.setter
    def src(self, value):
        self._set_attr("src", value)

# alt
    @property
    def alt(self):
        return self._get_attr("alt")

    @alt.setter
    def alt(self, value):
        self._set_attr("alt", value)

# title
    @property
    def title(self):
        return self._get_attr("title")

    @title.setter
    def title(self, value):
        self._set_attr("title", value)

# maximize_frame
    @property
    def maximize_frame(self):
        return self._get_attr("maximizeFrame")

    @maximize_frame.setter
    def maximize_frame(self, value):
        assert value == None or isinstance(value, bool), "maximize_frame must be a boolean"
        self._set_attr("maximizeFrame", value)