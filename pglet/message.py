from .utils import encode_attr
from .control import Control

# MessageButton
class MessageButton(Control):
    def __init__(self, text, action=None):
        Control.__init__(self)
        self.text = text
        self.action = action

    def _getControlName(self):
        return "button"

    # text
    @property
    def text(self):
        return self._get_attr("text")

    @text.setter
    def text(self, value):
        self._set_attr("text", value)

    # action
    @property
    def action(self):
        return self._get_attr("action")

    @action.setter
    def action(self, value):
        self._set_attr("action", value)

# Message
class Message(Control):
    def __init__(self, value=None, type=None, id=None,
            multiline=None, truncated=None, dismiss=None,
            data=None, ondismiss=None, buttons=[],
            width=None, height=None, padding=None, margin=None,
            visible=None, disabled=None):
        
        Control.__init__(self, id=id,
            width=width, height=height, padding=padding, margin=margin,
            visible=visible, disabled=disabled)
        
        self.type = type
        self.value = value
        self.multiline = multiline
        self.truncated = truncated
        self.dismiss = dismiss
        self.data = data
        self.ondismiss = ondismiss
        self._buttons = []
        if buttons and len(buttons) > 0:
            for button in buttons:
                self.add_button(button)
       

    def _getControlName(self):
        return "message"

    def add_button(self, button):
       if isinstance(button, MessageButton):
            self._buttons.append(button)
       else:
            self._buttons.append(MessageButton(str(button)))

# ondismiss
    @property
    def ondismiss(self):
        return None

    @ondismiss.setter
    def ondismiss(self, handler):
        self._add_event_handler("dismiss", handler)

# value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

# type
    @property
    def type(self):
        return self._get_attr("type")

    @type.setter
    def type(self, value):
        self._set_attr("type", value)

# multiline
    @property
    def multiline(self):
        return self._get_attr("multiline")

    @multiline.setter
    def multiline(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("multiline", value)

# truncated
    @property
    def truncated(self):
        return self._get_attr("truncated")

    @truncated.setter
    def truncated(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("truncated", value)

# dismiss
    @property
    def dismiss(self):
        return self._get_attr("dismiss")

    @dismiss.setter
    def dismiss(self, value):
        assert value == None or isinstance(value, bool), "value must be a boolean"
        self._set_attr("dismiss", value)

# data
    @property
    def data(self):
        return self._get_attr("data")

    @data.setter
    def data(self, value):
        self._set_attr("data", value)

    def _getChildren(self):
            return self._buttons