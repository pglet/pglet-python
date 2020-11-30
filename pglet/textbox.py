from .utils import *

class Textbox:
    def __init__(self, id=None, label=None, value=None, placeholder=None, errorMessage=None, description=None, multiline=False):
        self.id = id
        self.label = label
        self.value = value
        self.placeholder = placeholder
        self.errorMessage = errorMessage
        self.description = description
        self.multiline = multiline

    def __str__(self):
        parts = []
        parts.append("textbox")

        if self.id:
            parts.append(f"id=\"{encode_attr(self.id)}\"")

        if self.label:
            parts.append(f"label=\"{encode_attr(self.label)}\"")

        if self.value:
            parts.append(f"value=\"{encode_attr(self.value)}\"")            

        return " ".join(parts)