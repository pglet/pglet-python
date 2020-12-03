from .utils import encode_attr

class Control:
    def __init__(self, id=None, visible=None, disabled=None):
        self.id = id
        self.visible = visible
        self.disabled = disabled
    
    def _get_attrs_str(self, update=False):
        parts = []

        if update and not self.id:
            raise Exception("id attribute is not set")

        if self.id:
            parts.append(f"id=\"{encode_attr(self.id)}\"")

        if self.visible != None:
            parts.append(f"visible=\"{encode_attr(self.visible)}\"")

        if self.disabled != None:
            parts.append(f"disabled=\"{encode_attr(self.disabled)}\"")
        
        return parts