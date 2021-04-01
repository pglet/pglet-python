from .utils import encode_attr
from .control import Control

# Footer
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

class Panel(Control):
    def __init__(self, id=None, open=None, title=None, type=None,
            auto_dismiss=None, light_dismiss=None, width=None, blocking=None, data=None, 
            controls=None, footer=None, ondismiss=None, height=None,
            padding=None, margin=None, visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled, data=data)
        
        self.open = open
        self.title = title
        self.type = type
        self.auto_dismiss = auto_dismiss
        self.light_dismiss = light_dismiss
        self.width = width
        self.blocking = blocking
        self.ondismiss = ondismiss
        self.__footer = Footer(controls=footer)
        self.__controls = []
        if controls != None:
            for control in controls:
                self.__controls.append(control)

    def _get_control_name(self):
        return "panel"

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
    
    # ondismiss
    @property
    def ondismiss(self):
        return self._get_event_handler("dismiss")

    @ondismiss.setter
    def ondismiss(self, handler):
        self._add_event_handler("dismiss", handler)

    # open
    @property
    def open(self):
        return self._get_attr("open")

    @open.setter
    def open(self, value):
        assert value == None or isinstance(value, bool), "open must be a boolean"
        self._set_attr("open", value)

    # title
    @property
    def title(self):
        return self._get_attr("title")

    @title.setter
    def title(self, value):
        self._set_attr("title", value)

    # type
    @property
    def type(self):
        return self._get_attr("type")

    @type.setter
    def type(self, value):
        self._set_attr("type", value)

    # auto_dismiss
    @property
    def auto_dismiss(self):
        return self._get_attr("autoDismiss")

    @auto_dismiss.setter
    def auto_dismiss(self, value):
        assert value == None or isinstance(value, bool), "autoDismiss must be a boolean"
        self._set_attr("autoDismiss", value)

    # light_dismiss
    @property
    def light_dismiss(self):
        return self._get_attr("lightDismiss")

    @light_dismiss.setter
    def light_dismiss(self, value):
        assert value == None or isinstance(value, bool), "lightDismiss must be a boolean"
        self._set_attr("lightDismiss", value)

    # width
    @property
    def width(self):
        return self._get_attr("Width")

    @width.setter
    def width(self, value):
        self._set_attr("Width", value)

    # blocking
    @property
    def blocking(self):
        return self._get_attr("blocking")

    @blocking.setter
    def blocking(self, value):
        assert value == None or isinstance(value, bool), "blocking must be a boolean"
        self._set_attr("blocking", value)

    def _get_children(self):
        result=[]
        if self.__controls and len(self.__controls) > 0:
            for control in self.__controls:
                result.append(control)
        result.append(self.__footer)
        return result