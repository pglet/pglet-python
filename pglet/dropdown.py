from .utils import encode_attr
from .control import Control

class Dropdown(Control):

    class Option:
        pass

    def __init__(self, id=None, label=None, value=None, placeholder=None, errorMessage=None, options=[]):
        self.id = id
        self.label = label
        self.value = value
        self.placeholder = placeholder
        self.errorMessage = errorMessage
        self.options = options

    def add_option(self, option):
        pass

    def add_cmd(self):
        parts = []
        parts.append("dropdown")

        if self.id:
            parts.append(f"id=\"{encode_attr(self.id)}\"")

        return self.__props_str(parts)

    def update_cmd(self):
        parts = []

        if not self.id:
            raise Exception("id attribute is not set")

        parts.append(f"{encode_attr(self.id)}")

        return self.__props_str(parts)

    def __props_str(self, parts):
        if self.label:
            parts.append(f"label=\"{encode_attr(self.label)}\"")

        if self.value:
            parts.append(f"value=\"{encode_attr(self.value)}\"")

        if self.placeholder:
            parts.append(f"placeholder=\"{encode_attr(self.placeholder)}\"")

        if self.errorMessage:
            parts.append(f"errorMessage=\"{encode_attr(self.errorMessage)}\"")                     

        return " ".join(parts)