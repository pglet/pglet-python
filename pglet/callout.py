from pglet.control import Control


class Callout(Control):
    def __init__(
        self,
        id=None,
        target=None,
        position=None,
        gap=None,
        beak=None,
        beak_width=None,
        page_padding=None,
        focus=None,
        cover=None,
        visible=None,
        controls=None,
        on_dismiss=None,
        width=None,
        height=None,
        padding=None,
        margin=None,
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

        self.target = target
        self.position = position
        self.gap = gap
        self.beak = beak
        self.beak_width = beak_width
        self.page_padding = page_padding
        self.focus = focus
        self.cover = cover
        self.on_dismiss = on_dismiss
        self.__controls = []
        if controls != None:
            for control in controls:
                self.__controls.append(control)

    def _get_control_name(self):
        return "callout"

    # controls
    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value):
        self.__controls = value

    # on_dismiss
    @property
    def on_dismiss(self):
        return self._get_event_handler("dismiss")

    @on_dismiss.setter
    def on_dismiss(self, handler):
        self._add_event_handler("dismiss", handler)

    # target
    @property
    def target(self):
        return self._get_attr("target")

    @target.setter
    def target(self, value):
        self._set_attr("target", value)

    # position
    @property
    def position(self):
        return self._get_attr("position")

    @position.setter
    def position(self, value):
        self._set_attr("position", value)

    # gap
    @property
    def gap(self):
        return self._get_attr("gap")

    @gap.setter
    def gap(self, value):
        assert (
            value == None or isinstance(value, float) or isinstance(value, int)
        ), "gap must be a float"
        self._set_attr("gap", value)

    # beak
    @property
    def beak(self):
        return self._get_attr("beak")

    @beak.setter
    def beak(self, value):
        assert value == None or isinstance(value, bool), "beak must be a boolean"
        self._set_attr("beak", value)

    # beak_width
    @property
    def beak_width(self):
        return self._get_attr("beakWidth")

    @beak_width.setter
    def beak_width(self, value):
        assert (
            value == None or isinstance(value, float) or isinstance(value, int)
        ), "beak_width must be a float"
        self._set_attr("beakWidth", value)

    # page_padding
    @property
    def page_padding(self):
        return self._get_attr("pagePadding")

    @page_padding.setter
    def page_padding(self, value):
        assert (
            value == None or isinstance(value, float) or isinstance(value, int)
        ), "page_padding must be a float"
        self._set_attr("pagePadding", value)

    # focus
    @property
    def focus(self):
        return self._get_attr("focus")

    @focus.setter
    def focus(self, value):
        assert value == None or isinstance(value, bool), "focus must be a boolean"
        self._set_attr("focus", value)

    # cover
    @property
    def cover(self):
        return self._get_attr("cover")

    @cover.setter
    def cover(self, value):
        assert value == None or isinstance(value, bool), "cover must be a boolean"
        self._set_attr("cover", value)

    def _get_children(self):
        return self.__controls
