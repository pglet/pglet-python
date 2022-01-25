from pglet.control import Control

class IFrame(Control):
    def __init__(self, name=None, id=None, src=None, border=None, title=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.src = src
        self.border = border
        self.title = title

    def _get_control_name(self):
        return "iframe"

# src
    @property
    def src(self):
        return self._get_attr("src")

    @src.setter
    def src(self, value):
        self._set_attr("src", value)

# border
    @property
    def border(self):
        return self._get_attr("border")

    @border.setter
    def border(self, value):
        self._set_attr("border", value)

# title
    @property
    def title(self):
        return self._get_attr("title")

    @title.setter
    def title(self, value):
        self._set_attr("title", value)