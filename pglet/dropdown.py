from .utils import encode_attr
from .control import Control

class Option(Control):
    def __init__(self, key, text=None):
        self.key = key
        self.text = text

class Dropdown(Control):
    def __init__(self, id=None, label=None, value=None, placeholder=None,
            errorMessage=None, options=[], visible=None, disabled=None):
        Control.__init__(self, id=id, visible=visible, disabled=disabled)
        self.label = label
        self.value = value
        self.placeholder = placeholder
        self.errorMessage = errorMessage
        self.options = []
        if options and len(options) > 0:
            for option in options:
                self.add_option(option)

    def add_option(self, option):
        if isinstance(option, tuple) and len(option) > 1:
            # (key, value) tuple
            self.options.append(Option(option[0], option[1]))
        elif isinstance(option, Option):
            self.options.append(option)
        else:
            self.options.append(Option(str(option)))

    def get_cmd_str(self, update=False, indent='', index=None):
        lines = []

        # main command
        parts = []

        if not update:
            parts.append(indent + "dropdown")
        
        # base props
        parts.extend(Control._get_attrs_str(self, update))

        if self.label:
            parts.append(f"label=\"{encode_attr(self.label)}\"")

        if self.value:
            parts.append(f"value=\"{encode_attr(self.value)}\"")

        if self.placeholder:
            parts.append(f"placeholder=\"{encode_attr(self.placeholder)}\"")

        if self.errorMessage:
            parts.append(f"errorMessage=\"{encode_attr(self.errorMessage)}\"")

        lines.append(" ".join(parts))

        if index != None:
            index.append(self)

        # options
        if not update:
            for option in self.options:
                parts.clear()
                parts.append(indent + "  option")

                if option.key:
                    parts.append(f"key=\"{encode_attr(option.key)}\"")

                if option.text:
                    parts.append(f"text=\"{encode_attr(option.text)}\"")

                lines.append(" ".join(parts))

                if index != None:
                    index.append(option)

        return "\n".join(lines)