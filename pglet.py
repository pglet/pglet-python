import os
import pathlib
import platform
import subprocess
import re
import requests
import zipfile
import tarfile

PGLET_VERSION = "0.1.5"
pglet_exe = ""

class Connection:
    conn_id = ""
    url = ""
    public = False
    private = False

    def __init__(self, conn_id):
        self.conn_id = conn_id

    def f(self):
        return 'hello world'

def page(name='', public=False, private=False, server='', token=''):
    print (f"connecting to {name}")

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

def install():
    global pglet_exe
    isWindows = (platform.system() == "Windows")

    home = str(pathlib.Path.home())
    pglet_dir = os.path.join(home, ".pglet")
    pglet_bin = os.path.join(pglet_dir, "bin")

    if not os.path.exists(pglet_bin):
        os.makedirs(pglet_bin)
    
    if isWindows:
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
        if isWindows:
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

        if isWindows:
            with zipfile.ZipFile(temp_arch, 'r') as zip_arch:
                zip_arch.extractall(pglet_bin)
        else:
            with tarfile.open(temp_arch, 'r:gz') as tar_arch:
                tar_arch.extractall(pglet_bin)

        os.remove(temp_arch)

def cmp(a, b):
    return (a > b) - (a < b) 

def ver_cmp(version1, version2):
    def normalize(v):
        return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
    return cmp(normalize(version1), normalize(version2))

# install Pglet during import
install()