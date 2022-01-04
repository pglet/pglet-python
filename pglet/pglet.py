import logging
import os
import platform
import subprocess
import traceback
from threading import Thread
import threading
import traceback
import signal
from time import sleep
from urllib.parse import urlparse, urlunparse

from .reconnecting_websocket import ReconnectingWebSocket
from .utils import is_localhost_url, which
from .connection import Connection
from .page import Page
from .event import Event
from .constants import *

HOSTED_SERVICE_URL = "https://app.pglet.io"
CONNECT_TIMEOUT_SECONDS = 10

def page(name=None, local=False,  web=False, server=None, token=None, permissions=None, no_window=False):
    conn = _connect_internal(name, False, web, server, token, permissions, no_window)
    print("Page URL:", conn.page_url)
    page = Page(conn, ZERO_SESSION)
    conn.sessions[ZERO_SESSION] = page
    return page

def app(name=None, local=False, web=False, server=None, token=None, target=None, permissions=None, no_window=False):

    if target == None:
        raise Exception("target argument is not specified")

    conn = _connect_internal(name, True, web, server, token, permissions, no_window, target)
    print("App URL:", conn.page_url)

    terminate = threading.Event()

    def exit_gracefully(signum, frame):
        logging.debug("Gracefully terminating Pglet app")
        terminate.set()

    signal.signal(signal.SIGINT, exit_gracefully)
    signal.signal(signal.SIGTERM, exit_gracefully)

    try:
        print("Connected to Pglet app and handling user sessions...")
        terminate.wait()
    except (KeyboardInterrupt) as e:
        pass

    conn.close()

def _connect_internal(name=None, is_app=False, web=False, server=None, token=None, permissions=None, no_window=False, session_handler=None):
    if server == None and web:
        server = HOSTED_SERVICE_URL
    elif server == None:
        env_port = os.getenv('PGLET_SERVER_PORT')
        port = env_port if env_port != None and env_port != "" else "5000"
        server = f"http://localhost:{port}"

    connected = threading.Event()

    def on_event(conn, e):
        if e.sessionID in conn.sessions:
            conn.sessions[e.sessionID].on_event(Event(e.eventTarget, e.eventName, e.eventData))
            if e.eventTarget == "page" and e.eventName == "close":
                print("Session closed:", e.sessionID)
                del conn.sessions[e.sessionID]

    def on_session_created(conn, session_data):
        page = Page(conn, session_data.sessionID)
        conn.sessions[session_data.sessionID] = page
        print("Session started:", session_data.sessionID)
        try:
            session_handler(page)
        except Exception as e:
            print(f"Unhandled error processing page session {page.session_id}:", traceback.format_exc())
            page.error(f"There was an error while processing your request: {e}")                

    ws_url = _get_ws_url(server)
    ws = ReconnectingWebSocket(ws_url)
    conn = Connection(ws)
    conn.on_event = on_event

    if session_handler != None:
        conn.on_session_created = on_session_created

    def _on_ws_connect():
        if conn.page_name == None:
            conn.page_name = "*" if name == "" or name == None else name
        result = conn.register_host_client(conn.host_client_id, conn.page_name, is_app, token, permissions)
        conn.host_client_id = result.hostClientID
        conn.page_name = result.pageName
        conn.page_url = f"{server.rstrip('/')}/{result.pageName}"
        if not no_window and not conn.browser_opened:
            _open_browser(conn.page_url)
            conn.browser_opened = True
        connected.set()

    def _on_ws_failed_connect():
        logging.info(f"Failed to connect: {ws_url}")
        if is_localhost_url(ws_url):
            _start_pglet_server()

    ws.on_connect = _on_ws_connect
    ws.on_failed_connect = _on_ws_failed_connect
    ws.connect()
    for n in range(0, CONNECT_TIMEOUT_SECONDS):
        if not connected.is_set():
            sleep(1)
    if not connected.is_set():
        ws.close()
        raise Exception(f"Could not connected to Pglet server in {CONNECT_TIMEOUT_SECONDS} seconds.")

    return conn

def _start_pglet_server():
    print("Starting Pglet Server in local mode...")

    if _is_windows():
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
        if _is_windows():
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

    args = [pglet_exe, "server", "--background"]

    # auto-detect Replit environment
    if os.getenv("REPL_ID") != None:
        args.append("--attached")

    subprocess.run(args, check=True)

def _open_browser(url):
    if _is_windows():
        subprocess.run(["explorer.exe", url])
    elif _is_macos():
        subprocess.run(["open", url])

def _get_ws_url(server: str):
    url = server.rstrip('/')
    if server.startswith('https://'):
        url = url.replace('https://', 'wss://')
    elif server.startswith('http://'):
        url = url.replace('http://', 'ws://')
    else:
        url = 'ws://' + url
    return url + "/ws"

def _is_windows():
    return platform.system() == "Windows"

def _is_macos():
    return platform.system() == "Darwin"  

# Fix: https://bugs.python.org/issue35935
#if is_windows():
#    signal.signal(signal.SIGINT, signal.SIG_DFL)