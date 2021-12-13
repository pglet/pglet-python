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
from .utils import is_localhost_url, is_windows, open_browser, which, encode_attr
from .connection import Connection
from .page import Page

HOSTED_SERVICE_URL = "https://app.pglet.io"

def page(name=None, local=False,  web=False, server=None, token=None, permissions=None, no_window=False):

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

def app(name=None, local=False, web=False, server=None, token=None, target=None, permissions=None, no_window=False):

    if target == None:
        raise Exception("target argument is not specified")

    if server == None and web:
        server = HOSTED_SERVICE_URL
    elif server == None:
        server = "http://localhost:5000"

    def session_wrapper(target, page):
        try:
            target(page)
        except Exception as e:
            print(f"Unhandled error processing page session {page.connection.conn_id}:", e)
            page.error(f"There was an error while processing your request: {e}")        

    def on_session_created(conn, session_data):
        page = Page(conn, session_data.sessionID)

        # start page session in a new thread
        thread = Thread(target = session_wrapper, args = (target, page,))
        thread.start()

    ws_url = _get_ws_url(server)
    ws = ReconnectingWebSocket(ws_url)
    conn = Connection2(ws)
    conn.on_session_created = on_session_created

    def _on_ws_connect():
        print("Connected!")
        page_name = "*" if name == "" or name == None else name
        result = conn.register_host_client(conn.host_client_id, page_name, True, token, permissions)
        conn.host_client_id = result.hostClientID
        conn.page_name = result.pageName
        conn.page_url = f"{server}/{result.pageName}"
        if not no_window and not conn.browser_opened:
            open_browser(conn.page_url)
            conn.browser_opened = True

    def _on_ws_failed_connect():
        print(f"Failed to connect: {ws_url}")
        if is_localhost_url(ws_url):
            _start_pglet_server()

    ws.on_connect = _on_ws_connect
    ws.on_failed_connect = _on_ws_failed_connect
    ws.connect()

    try:
        print("Waiting for new app sessions. Press Enter to exit...")
        input()
    except (KeyboardInterrupt) as e:
        pass

    ws.close()

def _start_pglet_server():
    print("Starting Pglet Server in local mode...")

    if is_windows():
        pglet_exe = "pglet.exe"
    else:
        pglet_exe = "pglet"

    # check if pglet.exe is in PATH already (development mode)
    pglet_in_path = which(pglet_exe)
    if pglet_in_path:
        pglet_exe = pglet_in_path
    else:
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

    subprocess.run([pglet_exe, "server", "--background"], check=True)

def _get_ws_url(server: str):
    url = server.removesuffix('/')
    if server.startswith('https://'):
        url = url.replace('https://', 'wss://')
    elif server.startswith('http://'):
        url = url.replace('http://', 'ws://')
    else:
        url = 'ws://' + url
    return url + "/ws"

# Fix: https://bugs.python.org/issue35935
if is_windows():
    signal.signal(signal.SIGINT, signal.SIG_DFL)