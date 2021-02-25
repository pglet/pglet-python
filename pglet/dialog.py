from .utils import encode_attr
from .control import Control

# Footer
class Footer(Control):
    def __init__(self, id=None, controls=[]):
        Control.__init__(self, id=None)
    
        self._controls = []
        if controls and len(controls) > 0:
            for control in controls:
                self.add_control(control)

    # controls
    @property
    def controls(self):
        return self._controls

    def _getControlName(self):
        return "footer"

    def add_control(self, control):
        assert isinstance(control, Control), ("Footer can hold controls only")
        self._controls.append(control)

    def _getChildren(self):
        return self._controls

class Dialog(Control):
    def __init__(self, id=None, open=None, title=None, sub_text=None, large_header=None,
            auto_dismiss=None, width=None, max_width=None, height=None, fixed_top=None,
            blocking=None, data=None, controls=[], footer=[], ondismiss=None,
            padding=None, margin=None, visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.open = open
        self.title = title
        self.sub_text = sub_text
        self.large_header = large_header
        self.auto_dismiss = auto_dismiss
        self.max_width = max_width
        self.fixed_top = fixed_top
        self.blocking = blocking
        self.data = data
        self.ondismiss = ondismiss
        self._footer = Footer(controls=footer)
        self._controls = []
        if controls and len(controls) > 0:
            for control in controls:
                self.add_control(control)

    def _getControlName(self):
        return "dialog"

    def add_control(self, control):
        assert isinstance(control, Control), 'dialog can hold controls only'
        self._controls.append(control)

    # controls
    @property
    def controls(self):
        return self._controls

    # footer
    @property
    def footer(self):
        return self._footer 
    
    # ondismiss
    @property
    def ondismiss(self):
        return None

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

    # sub_text
    @property
    def sub_text(self):
        return self._get_attr("subText")

    @sub_text.setter
    def sub_text(self, value):
        self._set_attr("subText", value)

    # large_header
    @property
    def large_header(self):
        return self._get_attr("largeHeader")

    @large_header.setter
    def large_header(self, value):
        assert value == None or isinstance(value, bool), "large_header must be a boolean"
        self._set_attr("largeHeader", value)

    # auto_dismiss
    @property
    def auto_dismiss(self):
        return self._get_attr("autoDismiss")

    @auto_dismiss.setter
    def auto_dismiss(self, value):
        assert value == None or isinstance(value, bool), "autoDismiss must be a boolean"
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
    def fixed_top(self, value):
        assert value == None or isinstance(value, bool), "fixed_top must be a boolean"
        self._set_attr("fixedTop", value)

    # blocking
    @property
    def blocking(self):
        return self._get_attr("blocking")

    @blocking.setter
    def blocking(self, value):
        assert value == None or isinstance(value, bool), "blocking must be a boolean"
        self._set_attr("blocking", value)

    # data
    @property
    def data(self):
        return self._get_attr("data")

    @data.setter
    def data(self, value):
        self._set_attr("data", value)

    def _getChildren(self):
        result=[]
        if self._controls and len(self._controls) > 0:
            for control in self._controls:
                result.append(control)
        result.append(self._footer)
        return result