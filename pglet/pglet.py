import logging
import os
from pathlib import Path
import subprocess
import traceback
from threading import Thread
import threading
import traceback
import signal
from time import sleep
import urllib.request
import tempfile
import zipfile
import tarfile

from pglet.reconnecting_websocket import ReconnectingWebSocket
from pglet.utils import *
from pglet.connection import Connection
from pglet.page import Page
from pglet.event import Event
from pglet import constants

def page(name=None, local=False,  web=False, server=None, token=None, permissions=None, no_window=False):
    conn = _connect_internal(name, False, web, server, token, permissions, no_window)
    print("Page URL:", conn.page_url)
    page = Page(conn, constants.ZERO_SESSION)
    conn.sessions[constants.ZERO_SESSION] = page
    return page

def app(name=None, local=False, web=False, server=None, token=None, target=None, permissions=None, no_window=False):

    if target == None:
        raise Exception("target argument is not specified")

    conn = _connect_internal(name, True, web, server, token, permissions, no_window, target)
    print("App URL:", conn.page_url)

    terminate = threading.Event()

    def exit_gracefully(signum, frame):
        logging.debug("Gracefully terminating Pglet app...")
        terminate.set()

    signal.signal(signal.SIGINT, exit_gracefully)
    signal.signal(signal.SIGTERM, exit_gracefully)

    try:
        print("Connected to Pglet app and handling user sessions...")

        if is_windows():
            input()
        else:
            terminate.wait()
    except (Exception) as e:
        pass

    conn.close()

def _connect_internal(name=None, is_app=False, web=False, server=None, token=None, permissions=None, no_window=False, session_handler=None):
    if server == None and web:
        server = constants.HOSTED_SERVICE_URL
    elif server == None:
        env_port = os.getenv('PGLET_SERVER_PORT')
        port = env_port if env_port != None and env_port != "" else constants.PGLET_SERVER_DEFAULT_PORT
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
            open_in_browser(conn.page_url)
            conn.browser_opened = True
        connected.set()

    def _on_ws_failed_connect():
        logging.info(f"Failed to connect: {ws_url}")
        if is_localhost_url(ws_url):
            _start_pglet_server()

    ws.on_connect = _on_ws_connect
    ws.on_failed_connect = _on_ws_failed_connect
    ws.connect()
    for n in range(0, constants.CONNECT_TIMEOUT_SECONDS):
        if not connected.is_set():
            sleep(1)
    if not connected.is_set():
        ws.close()
        raise Exception(f"Could not connected to Pglet server in {constants.CONNECT_TIMEOUT_SECONDS} seconds.")

    return conn

def _start_pglet_server():
    print("Starting Pglet Server in local mode...")

    pglet_exe = "pglet.exe" if is_windows() else "pglet"

    # check if pglet.exe exists in "bin" directory (user mode)
    p = Path(__file__).parent.joinpath("bin", f"{get_platform()}-{get_arch()}", pglet_exe)
    if p.exists():
        pglet_path = str(p)
        logging.info(f"Pglet Server found in: {pglet_path}")
    else:
        # check if pglet.exe is in PATH (pglet developer mode)
        pglet_path = which(pglet_exe)
        if not pglet_path:
            # download pglet from GitHub (python module developer mode)
            pglet_path = _download_pglet()
        else:
            logging.info(f"Pglet Server found in PATH")

    # start Pglet server
    args = [pglet_path, "server", "--background"]

    # auto-detect Replit environment
    if os.getenv("REPL_ID") != None:
        args.append("--attached")

    subprocess.run(args, check=True)

def _get_ws_url(server: str):
    url = server.rstrip('/')
    if server.startswith('https://'):
        url = url.replace('https://', 'wss://')
    elif server.startswith('http://'):
        url = url.replace('http://', 'ws://')
    else:
        url = 'ws://' + url
    return url + "/ws"

def _download_pglet():
    pglet_exe = "pglet.exe" if is_windows() else "pglet"
    pglet_bin = Path.home().joinpath(".pglet", "bin")
    pglet_bin.mkdir(parents=True, exist_ok=True)

    pglet_version = _get_pglet_version()
    
    installed_ver = None
    pglet_path = pglet_bin.joinpath(pglet_exe)
    if pglet_path.exists():
        # check installed version
        installed_ver = subprocess.check_output([pglet_path, "--version"]).decode("utf-8")
        logging.info(f"Pglet v{pglet_version} is already installed in {pglet_path}")
    
    if not installed_ver or installed_ver != pglet_version:
        print(f"Downloading Pglet v{pglet_version} to {pglet_path}")

        ext = "zip" if is_windows() else "tar.gz"
        file_name = F"pglet-{pglet_version}-{get_platform()}-{get_arch()}.{ext}"
        pglet_url = f"https://github.com/pglet/pglet/releases/download/v{pglet_version}/{file_name}"

        temp_arch = Path(tempfile.gettempdir()).joinpath(file_name)
        try:
            urllib.request.urlretrieve(pglet_url, temp_arch)
            if is_windows():
                with zipfile.ZipFile(temp_arch, 'r') as zip_arch:
                    zip_arch.extractall(pglet_bin)
            else:
                with tarfile.open(temp_arch, 'r:gz') as tar_arch:
                    tar_arch.extractall(pglet_bin)            
        finally:
            os.remove(temp_arch)
    return pglet_path

def _get_pglet_version():
    appveyor_yml = Path(__file__).parent.parent.joinpath('appveyor.yml').absolute()

    version_prefix = "PGLET_VERSION:"
    with open(appveyor_yml) as yml:
        for line in yml:
            if version_prefix in line:
                return line.split(':')[1].strip()
    raise f"{version_prefix} not found in appveyor.yml"

# Fix: https://bugs.python.org/issue35935
# if _is_windows():
#    signal.signal(signal.SIGINT, signal.SIG_DFL)