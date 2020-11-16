import os
import pathlib
import platform
import subprocess
import re
import requests
import zipfile
import tarfile

PGLET_VERSION = "0.1.5"

def cmp(a, b):
    return (a > b) - (a < b) 

def mycmp(version1, version2):
    def normalize(v):
        return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
    return cmp(normalize(version1), normalize(version2))

def pglet_install():
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
    
    if not installed_ver or mycmp(installed_ver, ver) < 0:
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

pglet_install()