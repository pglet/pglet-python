import logging
from typing import List
from pglet.protocol import Command
from pglet.connection import Connection
from .control import Control
from .control_event import ControlEvent
from .constants import *
import json
import threading

class Page(Control):

    def __init__(self, conn: Connection, session_id):
        Control.__init__(self, id="page")
    
        self._conn = conn
        self._session_id = session_id
        self._controls = [] # page controls
        self._index = {} # index with all page controls
        self._index[self.id] = self
        self._last_event = None
        self._event_available = threading.Event()
        self._fetch_page_details()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def get_control(self, id):
        return self._index.get(id)

    def _get_children(self):
        return self._controls

    def _fetch_page_details(self):
        values = self._conn.send_commands(self._conn.page_name, self._session_id, [
            Command(0, 'get', ['page', 'hash'], None, None, None),
            Command(0, 'get', ['page', 'win_width'], None, None, None),
            Command(0, 'get', ['page', 'win_height'], None, None, None),
            Command(0, 'get', ['page', 'userid'], None, None, None),
            Command(0, 'get', ['page', 'userlogin'], None, None, None),
            Command(0, 'get', ['page', 'username'], None, None, None),
            Command(0, 'get', ['page', 'useremail'], None, None, None),
            Command(0, 'get', ['page', 'userclientip'], None, None, None)
        ]).results
        self._set_attr("hash", values[0], False)
        self._set_attr("win_width", values[1], False)
        self._set_attr("win_height", values[2], False)
        self._set_attr("userid", values[3], False)
        self._set_attr("userlogin", values[4], False)
        self._set_attr("username", values[5], False)
        self._set_attr("useremail", values[6], False)
        self._set_attr("userclientip", values[7], False)

    def update(self, *controls):
        with self._lock:
            if len(controls) == 0:
                return self.__update(self)
            else:
                return self.__update(*controls)

    def __update(self, *controls):
        added_controls = []
        commands = []

        # build commands
        for control in controls:
            control.build_update_commands(self._index, added_controls, commands)
        
        if len(commands) == 0:
            return

        # execute commands
        results = self._conn.send_commands(self._conn.page_name, self._session_id, commands).results

        if len(results) > 0:
            n = 0
            for line in results:
                for id in line.split(' '):
                    added_controls[n]._Control__uid = id
                    added_controls[n].page = self

                    # add to index
                    self._index[id] = added_controls[n]
                    n += 1

    def add(self, *controls):
        with self._lock:
            self._controls.extend(controls)
            return self.__update(self)

    def insert(self, at, *controls):
        with self._lock:
            n = at
            for control in controls:
                self._controls.insert(n, control)
                n += 1
            return self.__update(self)

    def remove(self, *controls):
        with self._lock:
            for control in controls:
                self._controls.remove(control)
            return self.__update(self)

    def remove_at(self, index):
        with self._lock:
            self._controls.pop(index)
            return self.__update(self)

    def clean(self):
        with self._lock:
            self._previous_children.clear()
            for child in self._get_children():
                self._remove_control_recursively(self._index, child)
            self._controls.clear()
            return self._send_command("clean", [self.uid])

    def error(self, message=""):
        with self._lock:
            self._send_command("error", [message])

    def on_event(self, e):
        logging.info(f"page.on_event: {e.target} {e.name} {e.data}")

        if e.target == "page" and e.name == "change":
            with self._lock:
                for props in json.loads(e.data):
                    id = props["i"]
                    if id in self._index:
                        for name in props:
                            if name != "i":
                                self._index[id]._set_attr(name, props[name], dirty=False)
        
        elif e.target in self._index:
            self._last_event = ControlEvent(e.target, e.name, e.data, self._index[e.target], self)
            handler = self._index[e.target].event_handlers.get(e.name)
            if handler:
                t = threading.Thread(target=handler, args=(self._last_event,), daemon=True)
                t.start()
            self._event_available.set()

    def wait_event(self):
        self._event_available.clear()
        self._event_available.wait()
        return self._last_event

    def show_signin(self, auth_providers="*", auth_groups=False, allow_dismiss=False):
        with self._lock:
            self.signin = auth_providers
            self.signin_groups = auth_groups
            self.signin_allow_dismiss = allow_dismiss
            self.__update(self)

        while True:
            e = self.wait_event()
            if e.control == self and e.name.lower() == "signin":
                return True
            elif e.control == self and e.name.lower() == "dismisssignin":
                return False
    
    def signout(self):
        return self._send_command("signout", None)

    def can_access(self, users_and_groups):
        return self._send_command("canAccess", [users_and_groups]).result.lower() == "true"
    
    def close(self):
        if self._session_id == ZERO_SESSION:
            self._conn.close()
        
    def _send_command(self, name: str, values: List[str]):
        return self._conn.send_command(self._conn.page_name, self._session_id, Command(0, name, values, None, None, None))      

# url
    @property
    def url(self):
        return self._conn.page_url

# name
    @property
    def name(self):
        return self._conn.page_name

# connection
    @property
    def connection(self):
        return self._conn

# index
    @property
    def index(self):
        return self._index

# session_id
    @property
    def session_id(self):
        return self._session_id

# controls
    @property
    def controls(self):
        return self._controls

    @controls.setter
    def controls(self, value):
        self._controls = value

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

# gap
    @property
    def gap(self):
        return self._get_attr("gap")

    @gap.setter
    def gap(self, value):
        self._set_attr("gap", value)

# padding
    @property
    def padding(self):
        return self._get_attr("padding")

    @padding.setter
    def padding(self, value):
        self._set_attr("padding", value)       

# bgcolor
    @property
    def bgcolor(self):
        return self._get_attr("bgcolor")

    @bgcolor.setter
    def bgcolor(self, value):
        self._set_attr("bgcolor", value)

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

# win_width
    @property
    def win_width(self):
        w = self._get_attr("win_width")
        if w != None and w != "":
            return int(w)
        return 0

# win_height
    @property
    def win_height(self):
        h = self._get_attr("win_height")
        if h != None and h != "":
            return int(h)
        return 0

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

# on_resize
    @property
    def on_resize(self):
        return self._get_event_handler("resize")

    @on_resize.setter
    def on_resize(self, handler):
        self._add_event_handler("resize", handler)