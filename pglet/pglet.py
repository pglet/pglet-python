import os
import platform
import subprocess
import re
import signal
from threading import Thread
import threading
from time import sleep
from urllib.parse import urlparse, urlunparse

from pglet.connection2 import Connection2

from .reconnecting_websocket import ReconnectingWebSocket
from .utils import is_windows, which, encode_attr
from .connection import Connection
from .page import Page

pglet_exe = ""
HOSTED_SERVICE_URL = "https://console.pglet.io"

def page(name=None, local=False, server=None, token=None, permissions=None, no_window=False):

    pargs = [pglet_exe, "page"]

    if name != None:
        pargs.append(name)
    
    if local:
        pargs.append("--local")

    if server != None:
        pargs.append("--server")
        pargs.append(server)

    if token != None:
        pargs.append("--token")
        pargs.append(token)

    if permissions != None:
        pargs.append("--permissions")
        pargs.append(permissions)

    if no_window:
        pargs.append("--no-window")

    pargs.append("--all-events")

    # execute pglet.exe and get connection ID
    exe_result = subprocess.check_output(pargs).decode("utf-8").strip()
    result_parts = re.split(r"\s", exe_result, 1)

    url = result_parts[1]
    print(url)

    conn = Connection(result_parts[0])
    return Page(conn, url)

def app(name=None, local=False, server=None, token=None, target=None, permissions=None, no_window=False):

    if target == None:
        raise Exception("target argument is not specified")

    if server == None:
        server = HOSTED_SERVICE_URL
    
    ws = ReconnectingWebSocket(_get_ws_url(server))
    ws.connect()

    conn = Connection2(ws)
    result = conn.register_host_client("", "page2", True, None, None)
    print(result)

    try:
        print("Waiting for new app sessions. Press Enter to exit...")
        input()
    except (KeyboardInterrupt) as e:
        pass

    ws.close()

def on_ws_message(data):
    print(f"message: {data}")

def _get_ws_url(server: str):
    url = server.removesuffix('/')
    if server.startswith('https://'):
        url = url.replace('https://', 'wss://')
    elif server.startswith('http://'):
        url = url.replace('http://', 'ws://')
    else:
        url = 'ws://' + url
    return url + "/ws"


def app2(name=None, local=False, server=None, token=None, target=None, permissions=None, no_window=False):

    if target == None:
        raise Exception("target argument is not specified")

    pargs = [pglet_exe, "app"]

    if name != None:
        pargs.append(name)
    
    if local:
        pargs.append("--local")

    if server != None:
        pargs.append("--server")
        pargs.append(server)

    if token != None:
        pargs.append("--token")
        pargs.append(token)

    if permissions != None:
        pargs.append("--permissions")
        pargs.append(permissions)

    if no_window:
        pargs.append("--no-window")
    
    pargs.append("--all-events")

    def session_wrapper(target, page):
        try:
            target(page)
        except Exception as e:
            print(f"Unhandled error processing page session {page.connection.conn_id}:", e)
            page.error(f"There was an error while processing your request: {e}")

    # execute pglet.exe and get connection ID
    page_url = ""
    proc = subprocess.Popen(pargs, bufsize=0, stdout = subprocess.PIPE)
    for bline in proc.stdout:
        line = bline.decode('utf-8').rstrip()
        if page_url == "":
            # 1st is URL
            page_url = line
            print(page_url)
        else:
            # connection ID
            conn_id = line

            # create connection object
            conn = Connection(conn_id)
            page = Page(conn, page_url)
            
            # start page session in a new thread
            thread = Thread(target = session_wrapper, args = (target, page,))
            thread.start()

def init():
    global pglet_exe

    if is_windows():
        pglet_exe = "pglet.exe"
    else:
        pglet_exe = "pglet"

    # check if pglet.exe is in PATH already (development mode)
    pglet_in_path = which(pglet_exe)
    if pglet_in_path:
        pglet_exe = pglet_in_path
        return

    bin_dir = os.path.join(os.path.dirname(__file__), "bin")

    p = platform.system()
    if is_windows():
        plat = "windows"
    elif p == "Linux":
        plat = "linux"
    elif p == "Darwin":
        plat = "darwin"
    else:
        raise Exception(f"Unsupported platform: {p}")

    a = platform.machine().lower()
    if a == "x86_64" or a == "amd64":
        arch = "amd64"
    elif a == "arm64" or a == "aarch64":
        arch = "arm64"
    elif a.startswith("arm"):
        arch = "arm"
    else:
        raise Exception(f"Unsupported architecture: {a}")

    pglet_exe = os.path.join(bin_dir, f"{plat}-{arch}", pglet_exe)

# init Pglet during import
#init()

# Fix: https://bugs.python.org/issue35935
#signal.signal(signal.SIGINT, signal.SIG_DFL)