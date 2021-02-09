from .utils import encode_attr
from .control import Control

class Text(Control):
    def __init__(self, id=None, value=None, align=None, verticalAlign=None,
            size=None, bold=None, italic=None, pre=None, nowrap=None,
            block=None, color=None, bgcolor=None, border=None,
            borderRadius=None, borderLeft=None, borderRight=None, borderTop=None, borderBottom=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):

        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)

        self.value = value
        self.align = align
        self.verticalAlign = verticalAlign
        self.size = size
        self.bold = bold
        self.italic = italic
        self.pre = pre
        self.nowrap = nowrap
        self.block = block
        self.color = color
        self.bgcolor = bgcolor
        self.border = border
        self.borderRadius = borderRadius
        self.borderLeft = borderLeft
        self.borderRight = borderRight
        self.borderTop = borderTop
        self.borderBottom = borderBottom

    def _getControlName(self):
        return "text"

# value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

# align
    @property
    def align(self):
        return self._get_attr("align")

    @align.setter
    def align(self, value):
        self._set_attr("align", value)

# verticalAlign
    @property
    def verticalAlign(self):
        return self._get_attr("verticalAlign")

    @verticalAlign.setter
    def verticalAlign(self, value):
        self._set_attr("verticalAlign", value)

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
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("pre", value)

# nowrap
    @property
    def nowrap(self):
        return self._get_attr("nowrap")

    @nowrap.setter
    def nowrap(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("nowrap", value)

# block
    @property
    def block(self):
        return self._get_attr("block")

    @block.setter
    def block(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("block", value)

# color
    @property
    def color(self):
        return self._get_attr("color")

    @color.setter
    def color(self, value):
        self._set_attr("color", value)

# bgcolor
    @property
    def bgcolor(self):
        return self._get_attr("bgcolor")

    @bgcolor.setter
    def bgcolor(self, value):
        self._set_attr("bgcolor", value)

# border
    @property
    def border(self):
        return self._get_attr("border")

    @border.setter
    def border(self, value):
        self._set_attr("border", value)

# borderRadius
    @property
    def borderRadius(self):
        return self._get_attr("borderRadius")

    @borderRadius.setter
    def borderRadius(self, value):
        self._set_attr("borderRadius", value)

# borderLeft
    @property
    def borderLeft(self):
        return self._get_attr("borderLeft")

    @borderLeft.setter
    def borderLeft(self, value):
        self._set_attr("borderLeft", value)

# borderRight
    @property
    def borderRight(self):
        return self._get_attr("borderRight")

    @borderRight.setter
    def borderRight(self, value):
        self._set_attr("borderRight", value)

# borderTop
    @property
    def borderTop(self):
        return self._get_attr("borderTop")

    @borderTop.setter
    def borderTop(self, value):
        self._set_attr("borderTop", value)

# borderBottom
    @property
    def borderBottom(self):
        return self._get_attr("borderBottom")

    @borderBottom.setter
    def borderBottom(self, value):
        self._set_attr("borderBottom", value)