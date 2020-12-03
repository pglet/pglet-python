from .utils import encode_attr

class Control:
    def __init__(self, id=None, visible=None, disabled=None):
        self._attrs = {}
        self._id = id
        self.visible = visible
        self.disabled = disabled

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def visible(self):
        return self._get_attr("visible")

    @visible.setter
    def visible(self, value):
        self._set_attr("visible", value)

    @property
    def disabled(self):
        return self._get_attr("disabled")

    @disabled.setter
    def disabled(self, value):
        self._set_attr("disabled", value)

    def _get_attr(self, name, defValue=None):
        if not name in self._attrs:
            return defValue
        return self._attrs[name]

    def _set_attr(self, name, value):
        if value == None:
            if name in self._attrs:
                del self._attrs[name]
            return
        self._attrs[name] = value
    
    def _get_attrs_str(self, update=False):
        parts = []

        if update and not self._id:
            raise Exception("id attribute is not set")

        if not update:
            # reset ID
            if self._id and self._id.startswith("_"):
                self._id = None
            elif self._id:
                self._id = self._id.split(":").pop()

        if self._id:
            parts.append(f'id="{encode_attr(self._id)}"')

        for attrName in sorted(self._attrs):
            val = self._attrs[attrName]
            sval = ""
            if isinstance(val, bool):
                sval = str(val).lower()
            else:
                sval = encode_attr(val)

            parts.append(f'{attrName}="{sval}"')
        
        return parts