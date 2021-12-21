import platform
import re
import subprocess

def is_windows():
    return platform.system() == "Windows"

def is_macos():
    return platform.system() == "Darwin"    

# https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, _ = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

def cmp(a, b):
    return (a > b) - (a < b) 

def ver_cmp(version1, version2):
    def normalize(v):
        return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
    return cmp(normalize(version1), normalize(version2))

def open_browser(url):
    if is_windows():
        subprocess.run(["explorer.exe", url])
    elif is_macos():
        subprocess.run(["open", url])

def is_localhost_url(url):
    return "://localhost/" in url or "://localhost:" in url