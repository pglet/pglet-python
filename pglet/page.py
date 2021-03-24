from .utils import encode_attr
from .control import Control

class Page(Control):

    def __init__(self, conn, url):
        Control.__init__(self, id="page")
    
        self.__conn = conn
        self.__url = url
        self.__controls = [] # page controls
        self.__index = {} # index with all page controls

    def get_control(self, id):
        return self.__index.get(id)

    def _get_children(self):
        return self.__controls

    def update(self, *controls):
        if len(controls) == 0:
            return self.__update(self)
        else:
            return self.__update(*controls)

    def __update(self, *controls):
        added_controls = []
        commands = []

        # build commands
        for control in controls:
            control.build_update_commands(self.__index, added_controls, commands)

        # execute commands
        ids = self.__conn.send_batch(commands)

        if ids != "":
            n = 0
            for line in ids.split('\n'):
                for id in line.split(' '):
                    added_controls[n].id = id
                    added_controls[n].page = self

                    # add to index
                    self.__index[id] = added_controls[n]
                    n += 1

    def add(self, *controls):
        self.__controls.extend(controls)
        return self.update()

    def insert(self, at, *controls):
        n = at
        for control in controls:
            self.__controls.insert(n, control)
            n += 1
        return self.update()

    def remove(self, *controls):
        for control in controls:
            self.__controls.remove(control)
        return self.update()

    def remove_at(self, index):
        self.__controls.pop(index)
        return self.update()

    def clean(self, force=False):
        if force:
            return self.__conn.send("clean page")
        else:
            self.__controls.clear()
            return self.update()

# connection
    @property
    def connection(self):
        return self.__conn

# url
    @property
    def url(self):
        return self.__url

# controls
    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value):
        self.__controls = value

# title
    @property
    def title(self):
        return self._get_attr("title")

    @title.setter
    def title(self, value):
        self._set_attr("title", value)

# vertical_fill
    @property
    def vertical_fill(self):
        return self._get_attr("verticalFill")

    @vertical_fill.setter
    def vertical_fill(self, value):
        assert value == None or isinstance(value, bool), "verticalFill must be a bool"
        self._set_attr("verticalFill", value)

# horizontal_align
    @property
    def horizontal_align(self):
        return self._get_attr("horizontalAlign")

    @horizontal_align.setter
    def horizontal_align(self, value):
        self._set_attr("horizontalAlign", value)

# vertical_align
    @property
    def vertical_align(self):
        return self._get_attr("verticalAlign")

    @vertical_align.setter
    def vertical_align(self, value):
        self._set_attr("verticalAlign", value)

# width
    @property
    def width(self):
        return self._get_attr("width")

    @width.setter
    def width(self, value):
        self._set_attr("width", value)

# padding
    @property
    def padding(self):
        return self._get_attr("padding")

    @padding.setter
    def padding(self, value):
        self._set_attr("padding", value)

# theme_primary_color
    @property
    def theme_primary_color(self):
        return self._get_attr("themePrimaryColor")

    @theme_primary_color.setter
    def theme_primary_color(self, value):
        self._set_attr("themePrimaryColor", value)

# theme_text_color
    @property
    def theme_text_color(self):
        return self._get_attr("themeTextColor")

    @theme_text_color.setter
    def theme_text_color(self, value):
        self._set_attr("themeTextColor", value)

# theme_background_color
    @property
    def theme_background_color(self):
        return self._get_attr("themeBackgroundColor")

    @theme_background_color.setter
    def theme_background_color(self, value):
        self._set_attr("themeBackgroundColor", value)