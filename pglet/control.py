from .utils import encode_attr

class Control:
    def __init__(self, id=None, visible=None, disabled=None):
        self._id = id
        self.visible = visible
        self.disabled = disabled

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
    
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
            parts.append(f"id=\"{encode_attr(self._id)}\"")

        if self.visible != None:
            parts.append(f"visible=\"{str(self.visible).lower()}\"")

        if self.disabled != None:
            parts.append(f"disabled=\"{str(self.disabled).lower()}\"")
        
        return parts