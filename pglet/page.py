from .utils import encode_attr
from .control import Control
from .alignment import Alignment

class Page(Control):

    def __init__(self, id=None, title=None, vertical_fill=None, horizontal_align=None,
            vertical_align=None, width=None, padding=None):
        Control.__init__(self, id="page")

        self.title = title
        self.vertical_fill = vertical_fill

        if horizontal_align != None and not isinstance(horizontal_align, Alignment):
            raise Exception("horizontalAlign must be of Alignment type")
        self.horizontal_align = horizontal_align

        if vertical_align != None and not isinstance(vertical_align, Alignment):
            raise Exception("verticalAlign must be of Alignment type")

        self.vertical_align = vertical_align
        self.width = width
        self.padding = padding

# title
    @property
    def title(self):
        return self._get_attr("title")

    @title.setter
    def title(self, value):
        self._set_attr("title", value)

# vertical_fill
    @property
    def vertical_fill(self):
        return self._get_attr("verticalFill")

    @vertical_fill.setter
    def vertical_fill(self, value):
        assert value == None or isinstance(value, bool), "verticalFill must be a bool"
        self._set_attr("verticalFill", value)

# horizontal_align
    @property
    def horizontal_align(self):
        return self._get_attr("horizontalAlign")

    @horizontal_align.setter
    def horizontal_align(self, value):
        assert value == None or isinstance(value, Alignment), "horizontalAlign must be an Alignment"
        self._set_attr("horizontalAlign", value)

# vertical_align
    @property
    def vertical_align(self):
        return self._get_attr("verticalAlign")

    @vertical_align.setter
    def vertical_align(self, value):
        assert value == None or isinstance(value, Alignment), "verticalAlign must be an Alignment"
        self._set_attr("verticalAlign", value)

# width
    @property
    def width(self):
        return self._get_attr("width")

    @width.setter
    def width(self, value):
        self._set_attr("width", value)

# padding
    @property
    def padding(self):
        return self._get_attr("padding")

    @padding.setter
    def padding(self, value):
        self._set_attr("padding", value)