import os
import pathlib
import platform
import subprocess
import re
import requests
import zipfile
import tarfile
from threading import Thread
from time import sleep

PGLET_VERSION = "0.1.6"
pglet_exe = ""

class Event:
    target = ""
    name = ""
    data = None

    def __init__(self, target, name, data):
        self.target = target
        self.name = name
        self.data = data

class Connection:
    conn_id = ""
    url = ""
    public = False
    private = False

    win_command_pipe = None
    win_event_pipe = None

    def __init__(self, conn_id):
        self.conn_id = conn_id

        if is_windows():
            self.__init_windows()
        else:
            self.__init_linux()
    
    def send(self, command):
        if is_windows():
            return self.__send_windows(command)
        else:
            return self.__send_linux(command)

    def wait_events(self):
        if is_windows():
            return self.__wait_events_windows()
        else:
            return self.__wait_events_linux()

    def __init_windows(self):
        self.win_command_pipe = open(rf'\\.\pipe\{self.conn_id}', 'r+b', buffering=0)
        self.win_event_pipe = open(rf'\\.\pipe\{self.conn_id}.events', 'r+b', buffering=0)

    def __send_windows(self, command):
        self.win_command_pipe.write(command.encode('utf-8'))
        r = self.win_command_pipe.readline().decode('utf-8').strip('\n')
        result_parts = re.split(r"\s", r, 1)
        if result_parts[0] == "error":
            raise Exception(result_parts[1])
        return result_parts[1]

    def __wait_events_windows(self):
        r = self.win_event_pipe.readline().decode('utf-8').strip('\n')
        result_parts = re.split(r"\s", r, 2)
        return Event(result_parts[0], result_parts[1], result_parts[2])

    def __init_linux(self):
        pass

    def __send_linux(self, command):
        pipe = open(rf'{self.conn_id}', "w")
        pipe.write(command)
        pipe.close()

        pipe = open(rf'{self.conn_id}', "r")
        r = pipe.readline()
        pipe.close()
        result_parts = re.split(r"\s", r, 1)
        if result_parts[0] == "error":
            raise Exception(result_parts[1])
        return result_parts[1]        

    def __wait_events_linux(self):
        pipe = open(rf'{self.conn_id}.events', "r")
        r = pipe.readline()
        pipe.close()
        result_parts = re.split(r"\s", r, 2)
        return Event(result_parts[0], result_parts[1], result_parts[2])        

    def close(self):
        raise Exception("Not implemented yet")

def page(name='', public=False, private=False, server='', token=''):
    #print (f"connecting to page {name}")

    pargs = [pglet_exe, "page"]

    if name != "":
        pargs.append(name)
    
    if public:
        pargs.append("--public")

    if private:
        pargs.append("--private")

    if server != "":
        pargs.append("--server")
        pargs.append(server)

    if token != "":
        pargs.append("--token")
        pargs.append(token)

    # execute pglet.exe and get connection ID
    exe_result = subprocess.check_output(pargs).decode("utf-8").strip()
    result_parts = re.split(r"\s", exe_result, 1)

    p = Connection(result_parts[0])
    p.url = result_parts[1]
    p.public = public
    p.private = private
    return p

def app(name='', public=False, private=False, server='', token='', target=None):
    #print (f"connecting to app {name}")

    if target == None:
        raise Exception("target argument is not specified")

    pargs = [pglet_exe, "app"]

    if name != "":
        pargs.append(name)
    
    if public:
        pargs.append("--public")

    if private:
        pargs.append("--private")

    if server != "":
        pargs.append("--server")
        pargs.append(server)

    if token != "":
        pargs.append("--token")
        pargs.append(token)

    # execute pglet.exe and get connection ID
    page_url = ""
    proc = subprocess.Popen(pargs, bufsize=0, stdout = subprocess.PIPE)
    for bline in proc.stdout:
        line = bline.decode('utf-8').rstrip()
        if page_url == "":
            # 1st is URL
            page_url = line
        else:
            # connection ID
            conn_id = line

            # create connection object
            p = Connection(conn_id)
            p.url = page_url
            p.public = public
            p.private = private

            # start page session in a new thread
            thread = Thread(target = target, args = (p,))
            thread.start()

def install():
    global pglet_exe

    home = str(pathlib.Path.home())
    pglet_dir = os.path.join(home, ".pglet")
    pglet_bin = os.path.join(pglet_dir, "bin")

    if not os.path.exists(pglet_bin):
        os.makedirs(pglet_bin)
    
    if is_windows():
        pglet_exe = os.path.join(pglet_bin, "pglet.exe")
    else:
        pglet_exe = os.path.join(pglet_bin, "pglet")

    ver = PGLET_VERSION

    installed_ver=None

    if os.path.exists(pglet_exe):
        # get installed pglet version
        installed_ver = subprocess.check_output([pglet_exe, "--version"]).decode("utf-8")
        print(f'Found Pglet v{installed_ver}')
    
    if not installed_ver or ver_cmp(installed_ver, ver) < 0:
        print(f'Installing Pglet v{PGLET_VERSION}...')

        p = platform.system()
        if is_windows():
            target = "windows-amd64.zip"
        elif p == "Linux":
            target = "linux-amd64.tar.gz"
        elif p == "Darwin":
            target = "darwin-amd64.tar.gz"
        else:
            raise Exception(f"Unsupported platform: {p}")

        # download archive
        pglet_url = f"https://github.com/pglet/pglet/releases/download/v{ver}/pglet-{target}"
        temp_arch = os.path.join(pglet_dir, target)

        #print (pglet_url)

        r = requests.get(pglet_url, allow_redirects=True)
        open(temp_arch, 'wb').write(r.content)

        if is_windows():
            with zipfile.ZipFile(temp_arch, 'r') as zip_arch:
                zip_arch.extractall(pglet_bin)
        else:
            with tarfile.open(temp_arch, 'r:gz') as tar_arch:
                tar_arch.extractall(pglet_bin)

        os.remove(temp_arch)

def is_windows():
    return platform.system() == "Windows"

def cmp(a, b):
    return (a > b) - (a < b) 

def ver_cmp(version1, version2):
    def normalize(v):
        return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
    return cmp(normalize(version1), normalize(version2))

# install Pglet during import
install()