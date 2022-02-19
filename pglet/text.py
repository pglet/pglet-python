from typing import List, Optional

from beartype import beartype

from pglet.control import (
    BorderColor,
    BorderRadius,
    BorderStyle,
    BorderWidth,
    Control,
    TextAlign,
    TextSize,
)

try:
    from typing import Literal
except:
    from typing_extensions import Literal


VerticalAlign = Literal[None, "top", "center", "bottom"]


class Text(Control):
    def __init__(
        self,
        value=None,
        id=None,
        markdown=None,
        align: TextAlign = None,
        vertical_align: VerticalAlign = None,
        size: TextSize = None,
        bold=None,
        italic=None,
        pre=None,
        nowrap=None,
        block=None,
        color=None,
        bgcolor=None,
        border_style: BorderStyle = None,
        border_width: BorderWidth = None,
        border_color: BorderColor = None,
        border_radius: BorderRadius = None,
        width=None,
        height=None,
        padding=None,
        margin=None,
        visible=None,
        disabled=None,
    ):

        Control.__init__(
            self,
            id=id,
            width=width,
            height=height,
            padding=padding,
            margin=margin,
            visible=visible,
            disabled=disabled,
        )

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
        self.border_style = border_style
        self.border_width = border_width
        self.border_color = border_color
        self.border_radius = border_radius

    def _get_control_name(self):
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
    @beartype
    def markdown(self, value: Optional[bool]):
        self._set_attr("markdown", value)

    # align
    @property
    def align(self):
        return self._get_attr("align")

    @align.setter
    @beartype
    def align(self, value: TextAlign):
        self._set_attr("align", value)

    # vertical_align
    @property
    def vertical_align(self):
        return self._get_attr("verticalAlign")

    @vertical_align.setter
    @beartype
    def vertical_align(self, value: VerticalAlign):
        self._set_attr("verticalAlign", value)

    # size
    @property
    def size(self):
        return self._get_attr("size")

    @size.setter
    @beartype
    def size(self, value: TextSize):
        self._set_attr("size", value)

    # bold
    @property
    def bold(self):
        return self._get_attr("bold")

    @bold.setter
    @beartype
    def bold(self, value: Optional[bool]):
        self._set_attr("bold", value)

    # italic
    @property
    def italic(self):
        return self._get_attr("italic")

    @italic.setter
    @beartype
    def italic(self, value: Optional[bool]):
        self._set_attr("italic", value)

    # pre
    @property
    def pre(self):
        return self._get_attr("pre")

    @pre.setter
    @beartype
    def pre(self, value: Optional[bool]):
        self._set_attr("pre", value)

    # nowrap
    @property
    def nowrap(self):
        return self._get_attr("nowrap")

    @nowrap.setter
    @beartype
    def nowrap(self, value: Optional[bool]):
        self._set_attr("nowrap", value)

    # block
    @property
    def block(self):
        return self._get_attr("block")

    @block.setter
    @beartype
    def block(self, value: Optional[bool]):
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

    # border_style
    @property
    def border_style(self):
        return self._get_value_or_list_attr("borderStyle", " ")

    @border_style.setter
    @beartype
    def border_style(self, value: BorderStyle):
        self._set_value_or_list_attr("borderStyle", value, " ")

    # border_width
    @property
    def border_width(self):
        return self._get_value_or_list_attr("borderWidth", " ")

    @border_width.setter
    @beartype
    def border_width(self, value: BorderWidth):
        self._set_value_or_list_attr("borderWidth", value, " ")

    # border_color
    @property
    def border_color(self):
        return self._get_value_or_list_attr("borderColor", " ")

    @border_color.setter
    @beartype
    def border_color(self, value: BorderColor):
        self._set_value_or_list_attr("borderColor", value, " ")

    # border_radius
    @property
    def border_radius(self):
        return self._get_value_or_list_attr("borderRadius", " ")

    @border_radius.setter
    @beartype
    def border_radius(self, value: BorderRadius):
        self._set_value_or_list_attr("borderRadius", value, " ")
