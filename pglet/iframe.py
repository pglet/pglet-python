from beartype import beartype
from pglet.control import Control, BORDER_STYLE


class IFrame(Control):
    def __init__(
        self,
        id=None,
        src=None,
        border=None,
        border_style: BORDER_STYLE = None,
        border_width=None,
        border_color=None,
        border_radius=None,
        title=None,
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

        self.src = src
        self.border = border
        self.border_style = border_style
        self.border_width = border_width
        self.border_color = border_color
        self.border_radius = border_radius
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

    # border_style
    @property
    def border_style(self):
        return self._get_attr("borderStyle")

    @border_style.setter
    @beartype
    def border_style(self, value: BORDER_STYLE):
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

    # title
    @property
    def title(self):
        return self._get_attr("title")

    @title.setter
    def title(self, value):
        self._set_attr("title", value)
