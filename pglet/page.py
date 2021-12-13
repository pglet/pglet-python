from .utils import encode_attr
from .control import Control
from .control_event import ControlEvent
import json
import threading

class Page(Control):

    def __init__(self, conn, session_id):
        Control.__init__(self, id="page")
    
        self.__conn = conn
        self.__session_id = session_id
        self.__controls = [] # page controls
        self.__index = {} # index with all page controls
        self.__index[self.id] = self
        #self.__fetch_page_details()

    def get_control(self, id):
        return self.__index.get(id)

    def _get_children(self):
        return self.__controls

    def __fetch_page_details(self):
        values = self.__conn.send_batch([
            'get page hash',
            'get page userid',
            'get page userlogin',
            'get page username',
            'get page useremail',
            'get page userclientip'
        ])
        self.hash = values[0]
        self.user_id = values[1]
        self.user_login = values[2]
        self.user_name = values[3]
        self.user_email = values[4]
        self.user_client_ip = values[5]

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
        
        if len(commands) == 0:
            return

        # execute commands
        result = self.__conn.send_batch(commands)

        if len(result) > 0:
            n = 0
            for line in result:
                for id in line.split(' '):
                    added_controls[n]._Control__uid = id
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

    def clean(self):
        self._previous_children.clear()
        for child in self._get_children():
            self._remove_control_recursively(self.__index, child)
        return self.__conn.send(f"clean {self.uid}")

    def error(self, message=""):
        self.__conn.send(f"error \"{encode_attr(message)}\"")

    def close(self):
        self.__conn.send("close")        

    def __on_event(self, e):
        #print("on_event:", e.target, e.name, e.data)

        if e.target == "page" and e.name == "change":
            all_props = json.loads(e.data)

            for props in all_props:
                id = props["i"]
                if id in self.__index:
                    for name in props:
                        if name != "i":
                            self.__index[id]._set_attr(name, props[name], dirty=False)
        
        elif e.target in self.__index:
            handler = self.__index[e.target].event_handlers.get(e.name)
            if handler:
                ce = ControlEvent(e.target, e.name, e.data, self.__index[e.target], self)
                t = threading.Thread(target=handler, args=(ce,), daemon=True)
                t.start()

    def wait_event(self):
        e = self.__conn.wait_event()
        return ControlEvent(e.target, e.name, e.data, self.__index[e.target], self)

    def show_signin(self, auth_providers="*", auth_groups=False, allow_dismiss=False):
        self.signin = auth_providers
        self.signin_groups = auth_groups
        self.signin_allow_dismiss = allow_dismiss
        self.update()

        while True:
            e = self.wait_event()
            if e.control == self and e.name.lower() == "signin":
                return True
            elif e.control == self and e.name.lower() == "dismisssignin":
                return False
    
    def signout(self):
        return self.__conn.send("signout")

    def can_access(self, users_and_groups):
        return self.__conn.send(f"canAccess \"{encode_attr(users_and_groups)}\"").lower() == "true"

# connection
    @property
    def connection(self):
        return self.__conn

# index
    @property
    def index(self):
        return self.__index

# session_id
    @property
    def session_id(self):
        return self.__session_id

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

# theme
    @property
    def theme(self):
        return self._get_attr("theme")

    @theme.setter
    def theme(self, value):
        self._set_attr("theme", value)

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

# hash
    @property
    def hash(self):
        return self._get_attr("hash")

    @hash.setter
    def hash(self, value):
        self._set_attr("hash", value)

# signin
    @property
    def signin(self):
        return self._get_attr("signin")

    @signin.setter
    def signin(self, value):
        self._set_attr("signin", value)

# signin_allow_dismiss
    @property
    def signin_allow_dismiss(self):
        return self._get_attr("signinAllowDismiss")

    @signin_allow_dismiss.setter
    def signin_allow_dismiss(self, value):
        self._set_attr("signinAllowDismiss", value)

# signin_groups
    @property
    def signin_groups(self):
        return self._get_attr("signinGroups")

    @signin_groups.setter
    def signin_groups(self, value):
        self._set_attr("signinGroups", value)

# user_id
    @property
    def user_id(self):
        return self._get_attr("userId")

    @user_id.setter
    def user_id(self, value):
        self._set_attr("userId", value)        

# user_login
    @property
    def user_login(self):
        return self._get_attr("userLogin")

    @user_login.setter
    def user_login(self, value):
        self._set_attr("userLogin", value)                

# user_name
    @property
    def user_name(self):
        return self._get_attr("userName")

    @user_name.setter
    def user_name(self, value):
        self._set_attr("userName", value)

# user_email
    @property
    def user_email(self):
        return self._get_attr("userEmail")

    @user_email.setter
    def user_email(self, value):
        self._set_attr("userEmail", value)

# user_client_ip
    @property
    def user_client_ip(self):
        return self._get_attr("userClientIP")

    @user_client_ip.setter
    def user_client_ip(self, value):
        self._set_attr("userClientIP", value)

# on_signin
    @property
    def on_signin(self):
        return self._get_event_handler("signin")

    @on_signin.setter
    def on_signin(self, handler):
        self._add_event_handler("signin", handler)

# on_dismiss_signin
    @property
    def on_dismiss_signin(self):
        return self._get_event_handler("dismissSignin")

    @on_dismiss_signin.setter
    def on_dismiss_signin(self, handler):
        self._add_event_handler("dismissSignin", handler)

# on_signout
    @property
    def on_signout(self):
        return self._get_event_handler("signout")

    @on_signout.setter
    def on_signout(self, handler):
        self._add_event_handler("signout", handler)        

# on_close
    @property
    def on_close(self):
        return self._get_event_handler("close")

    @on_close.setter
    def on_close(self, handler):
        self._add_event_handler("close", handler)

# on_hash_change
    @property
    def on_hash_change(self):
        return self._get_event_handler("hashChange")

    @on_hash_change.setter
    def on_hash_change(self, handler):
        self._add_event_handler("hashChange", handler)