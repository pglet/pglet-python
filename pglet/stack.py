from .utils import encode_attr
from .control import Control
#from .alignment import Alignment

class Stack(Control):

    def __init__(self, controls=[], id=None, horizontal=None, vertical_fill=None, horizontal_align=None,
            vertical_align=None, min_width=None, max_width=None, min_height=None, max_height=None, 
            gap=None, wrap=None, bgcolor=None, border=None, border_radius=None, border_left=None, 
            border_right=None, border_top=None, border_bottom=None, scrollx=None, scrolly=None,
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)

        self.horizontal = horizontal
        self.vertical_fill = vertical_fill
        self.horizontal_align = horizontal_align
        self.vertical_align = vertical_align
        self.min_width = min_width
        self.max_width = max_width
        self.min_height = min_height
        self.max_height = max_height
        self.gap = gap
        self.wrap = wrap
        self.bgcolor = bgcolor
        self.border = border
        self.border_radius = border_radius
        self.border_left = border_left
        self.border_right = border_right
        self.border_top = border_top
        self.border_bottom = border_bottom
        self.scrollx = scrollx
        self.scrolly = scrolly
        self._controls = controls

    def _get_control_name(self):
        return "stack"

# controls
    @property
    def controls(self):
        return self._controls

    @controls.setter
    def controls(self, value):
        self._controls = value

# horizontal
    @property
    def horizontal(self):
        return self._get_attr("horizontal")

    @horizontal.setter
    def horizontal(self, value):
        assert value == None or isinstance(value, bool), "horizontal must be a bool"
        self._set_attr("horizontal", value)

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
        self._set_attr("horizontalAlign", value)

# vertical_align
    @property
    def vertical_align(self):
        return self._get_attr("verticalAlign")

    @vertical_align.setter
    def vertical_align(self, value):
        self._set_attr("verticalAlign", value)

# min_width
    @property
    def min_width(self):
        return self._get_attr("minWidth")

    @min_width.setter
    def min_width(self, value):
        self._set_attr("minWidth", value)

# max_width
    @property
    def max_width(self):
        return self._get_attr("maxWidth")

    @max_width.setter
    def max_width(self, value):
        self._set_attr("maxWidth", value)

# min_height
    @property
    def min_height(self):
        return self._get_attr("minHeight")

    @min_height.setter
    def min_height(self, value):
        self._set_attr("minHeight", value)

# max_height
    @property
    def max_height(self):
        return self._get_attr("maxHeight")

    @max_height.setter
    def max_height(self, value):
        self._set_attr("maxHeight", value)
    
# gap
    @property
    def gap(self):
        return self._get_attr("gap")

    @gap.setter
    def gap(self, value):
        self._set_attr("gap", value)

# wrap
    @property
    def wrap(self):
        return self._get_attr("wrap")

    @wrap.setter
    def wrap(self, value):
        assert value == None or isinstance(value, bool), "wrap must be a bool"
        self._set_attr("wrap", value)

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

# scrollx
    @property
    def scrollx(self):
        return self._get_attr("scrollx")

    @scrollx.setter
    def scrollx(self, value):
        assert value == None or isinstance(value, bool), "scrollx must be a bool"
        self._set_attr("scrollx", value)

# scrolly
    @property
    def scrolly(self):
        return self._get_attr("scrolly")

    @scrolly.setter
    def scrolly(self, value):
        assert value == None or isinstance(value, bool), "scrolly must be a bool"
        self._set_attr("scrolly", value)



    def _get_children(self):
        return self._controls