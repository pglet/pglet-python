from typing import Optional
try:
    from typing import Literal
except:
    from typing_extensions import Literal

from beartype import beartype

from pglet.control import Control

DialogType = Literal[None, "normal", "largeHeader", "close"]


class Dialog(Control):
    def __init__(
        self,
        id=None,
        open=None,
        title=None,
        sub_text=None,
        type: DialogType = None,
        auto_dismiss=None,
        width=None,
        max_width=None,
        height=None,
        fixed_top=None,
        blocking=None,
        data=None,
        controls=None,
        footer=None,
        on_dismiss=None,
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
            data=data,
        )

        self.open = open
        self.title = title
        self.sub_text = sub_text
        self.type = type
        self.auto_dismiss = auto_dismiss
        self.max_width = max_width
        self.fixed_top = fixed_top
        self.blocking = blocking
        self.on_dismiss = on_dismiss
        self.__footer = Footer(controls=footer)
        self.__controls = []
        if controls != None:
            for control in controls:
                self.__controls.append(control)

    def _get_control_name(self):
        return "dialog"

    # controls
    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value):
        self.__controls = value

    # footer
    @property
    def footer(self):
        return self.__footer

    # on_dismiss
    @property
    def on_dismiss(self):
        return self._get_event_handler("dismiss")

    @on_dismiss.setter
    def on_dismiss(self, handler):
        self._add_event_handler("dismiss", handler)

    # open
    @property
    def open(self):
        return self._get_attr("open")

    @open.setter
    @beartype
    def open(self, value: Optional[bool]):
        self._set_attr("open", value)

    # title
    @property
    def title(self):
        return self._get_attr("title")

    @title.setter
    def title(self, value):
        self._set_attr("title", value)

    # sub_text
    @property
    def sub_text(self):
        return self._get_attr("subText")

    @sub_text.setter
    def sub_text(self, value):
        self._set_attr("subText", value)

    # type
    @property
    def type(self):
        return self._get_attr("type")

    @type.setter
    @beartype
    def type(self, value: DialogType):
        self._set_attr("type", value)

    # auto_dismiss
    @property
    def auto_dismiss(self):
        return self._get_attr("autoDismiss")

    @auto_dismiss.setter
    @beartype
    def auto_dismiss(self, value: Optional[bool]):
        self._set_attr("autoDismiss", value)

    # max_width
    @property
    def max_width(self):
        return self._get_attr("maxWidth")

    @max_width.setter
    def max_width(self, value):
        self._set_attr("maxWidth", value)

    # fixed_top
    @property
    def fixed_top(self):
        return self._get_attr("fixedTop")

    @fixed_top.setter
    @beartype
    def fixed_top(self, value: Optional[bool]):
        self._set_attr("fixedTop", value)

    # blocking
    @property
    def blocking(self):
        return self._get_attr("blocking")

    @blocking.setter
    @beartype
    def blocking(self, value: Optional[bool]):
        self._set_attr("blocking", value)

    def _get_children(self):
        result = []
        if self.__controls and len(self.__controls) > 0:
            for control in self.__controls:
                result.append(control)
        result.append(self.__footer)
        return result


class Footer(Control):
    def __init__(self, id=None, controls=None):
        Control.__init__(self, id=id)

        self.__controls = []
        if controls != None:
            for control in controls:
                self.__controls.append(control)

    # controls
    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value):
        self.__controls = value

    def _get_control_name(self):
        return "footer"

    def _get_children(self):
        return self.__controls
