from .utils import encode_attr
from .control import Control

class Text(Control):
    def __init__(self, value=None, id=None, markdown=None, align=None, vertical_align=None,
            size=None, bold=None, italic=None, pre=None, nowrap=None,
            block=None, color=None, bgcolor=None, border=None, border_style=None, border_width=None,
            border_color=None, border_radius=None, border_left=None, border_right=None, border_top=None, 
            border_bottom=None, width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):

        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)

        self.value = value
        self.markdown = markdown
        self.align = align
        self.vertical_align = vertical_align
        self.size = size
        self.bold = bold
        self.italic = italic
        self.pre = pre
        self.nowrap = nowrap
        self.block = block
        self.color = color
        self.bgcolor = bgcolor
        self.border = border
        self.border_style = border_style
        self.border_width = border_width
        self.border_color = border_color
        self.border_radius = border_radius
        self.border_left = border_left
        self.border_right = border_right
        self.border_top = border_top
        self.border_bottom = border_bottom

    def _getControlName(self):
        return "text"

# value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

# markdown
    @property
    def markdown(self):
        return self._get_attr("markdown")

    @markdown.setter
    def markdown(self, value):
        assert value == None or isinstance(value, bool), "markdown must be a boolean"
        self._set_attr("markdown", value)

# align
    @property
    def align(self):
        return self._get_attr("align")

    @align.setter
    def align(self, value):
        self._set_attr("align", value)

# vertical_align
    @property
    def vertical_align(self):
        return self._get_attr("verticalAlign")

    @vertical_align.setter
    def vertical_align(self, value):
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

# border_style
    @property
    def border_style(self):
        return self._get_attr("borderStyle")

    @border_style.setter
    def border_style(self, value):
        self._set_attr("borderStyle", value)

# border_width
    @property
    def border_width(self):
        return self._get_attr("borderWidth")

    @border_width.setter
    def border_width(self, value):
        self._set_attr("borderWidth", value)

# border_color
    @property
    def border_color(self):
        return self._get_attr("borderColor")

    @border_color.setter
    def border_color(self, value):
        self._set_attr("borderColor", value)

# border_radius
    @property
    def border_radius(self):
        return self._get_attr("borderRadius")

    @border_radius.setter
    def border_radius(self, value):
        self._set_attr("borderRadius", value)

# border_left
    @property
    def border_left(self):
        return self._get_attr("borderLeft")

    @border_left.setter
    def border_left(self, value):
        self._set_attr("borderLeft", value)

# border_right
    @property
    def border_right(self):
        return self._get_attr("borderRight")

    @border_right.setter
    def border_right(self, value):
        self._set_attr("borderRight", value)

# border_top
    @property
    def border_top(self):
        return self._get_attr("borderTop")

    @border_top.setter
    def border_top(self, value):
        self._set_attr("borderTop", value)

# border_bottom
    @property
    def border_bottom(self):
        return self._get_attr("borderBottom")

    @border_bottom.setter
    def border_bottom(self, value):
        self._set_attr("borderBottom", value)