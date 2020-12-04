from .utils import encode_attr
from .control import Control
from .alignment import Alignment

class Page(Control):

    def __init__(self, id=None, title=None, verticalFill=None, horizontalAlign=None,
            verticalAlign=None, width=None, padding=None):
        Control.__init__(self, id="page")

        self.title = title
        self.verticalFill = verticalFill

        if horizontalAlign != None and not isinstance(horizontalAlign, Alignment):
            raise Exception("horizontalAlign must be of Alignment type")
        self.horizontalAlign = horizontalAlign

        if verticalAlign != None and not isinstance(verticalAlign, Alignment):
            raise Exception("verticalAlign must be of Alignment type")

        self.verticalAlign = verticalAlign
        self.width = width
        self.padding = padding

# title
    @property
    def title(self):
        return self._get_attr("title")

    @title.setter
    def title(self, value):
        self._set_attr("title", value)

# verticalFill
    @property
    def verticalFill(self):
        return self._get_attr("verticalFill")

    @verticalFill.setter
    def verticalFill(self, value):
        assert value == None or isinstance(value, bool), "verticalFill must be a bool"
        self._set_attr("verticalFill", value)

# horizontalAlign
    @property
    def horizontalAlign(self):
        return self._get_attr("horizontalAlign")

    @horizontalAlign.setter
    def horizontalAlign(self, value):
        assert value == None or isinstance(value, Alignment), "horizontalAlign must be an Alignment"
        self._set_attr("horizontalAlign", value)

# verticalAlign
    @property
    def verticalAlign(self):
        return self._get_attr("verticalAlign")

    @verticalAlign.setter
    def verticalAlign(self, value):
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