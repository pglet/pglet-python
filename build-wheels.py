import hashlib
import io
import os
import pathlib
import shutil
import stat
import sys
import urllib.request
import zipfile
from base64 import urlsafe_b64encode

import tomli

# https://www.python.org/dev/peps/pep-0425/
# https://www.python.org/dev/peps/pep-0600/

# pglet-0.1.0-py3-none-win_amd64.whl
# pglet-0.1.0-py3-none-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl
# pglet-0.1.0-py3-none-manylinux_2_12_aarch64.manylinux2010_aarch64.manylinux_2_17_aarch64.manylinux2014_aarch64.whl
# pglet-0.1.0-py3-none-manylinux_2_12_armv7l.manylinux2010_armv7l.manylinux_2_17_armv7l.manylinux2014_armv7l.whl
# pglet-0.1.0-py3-none-macosx_11_0_arm64.whl
# pglet-0.1.0-py3-none-macosx_10_9_x86_64.whl

# Tag: cp37-cp37m-manylinux_2_12_x86_64
# Tag: cp37-cp37m-manylinux2010_x86_64
# Tag: cp37-cp37m-manylinux_2_17_x86_64
# Tag: cp37-cp37m-manylinux2014_x86_64
# Tag: cp39-cp39-macosx_10_9_x86_64
# Tag: cp38-cp38-win_amd64

# Download pglet executable to `pglet/bin/pglet`
# pglet-{version}.dist-info/WHEEL
#   Tag: py3-none-any -> with actual tags
# pglet-{version}.dist-info/RECORD
#   Add record for `pglet/bin/pglet`
#   Add record for `pglet-{version}.dist-info/WHEEL`

packages = {
    "Windows amd64": {
        "asset": "windows-amd64.exe",
        "exec": "pglet.exe",
        "wheel_tags": ["py3-none-win_amd64"],
        "file_suffix": "py3-none-win_amd64",
    },
    "Linux amd64": {
        "asset": "linux-amd64",
        "exec": "pglet",
        "wheel_tags": [
            "py3-none-manylinux_2_17_x86_64",
            "py3-none-manylinux2014_x86_64",
        ],
        "file_suffix": "py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64",
    },
    "Linux arm64": {
        "asset": "linux-arm64",
        "exec": "pglet",
        "wheel_tags": [
            "py3-none-manylinux_2_17_aarch64",
            "py3-none-manylinux2014_aarch64",
        ],
        "file_suffix": "py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64",
    },
    "Linux arm": {
        "asset": "linux-arm",
        "exec": "pglet",
        "wheel_tags": [
            "py3-none-manylinux_2_17_armv7l",
            "py3-none-manylinux2014_armv7l",
        ],
        "file_suffix": "py3-none-manylinux_2_17_armv7l.manylinux2014_armv7l",
    },
    "macOS amd64": {
        "asset": "darwin-amd64",
        "exec": "pglet",
        "wheel_tags": ["py3-none-macosx_10_9_x86_64"],
        "file_suffix": "py3-none-macosx_10_9_x86_64",
    },
    "macOS arm64": {
        "asset": "darwin-arm64",
        "exec": "pglet",
        "wheel_tags": ["py3-none-macosx_11_0_arm64"],
        "file_suffix": "py3-none-macosx_11_0_arm64",
    },
}


def unpack_zip(zip_path, dest_dir):
    zf = zipfile.ZipFile(zip_path)
    zf.extractall(path=dest_dir)


def download_pglet(version, suffix, dest_file):
    file_name = f"pglet-{version}-{suffix}"
    pglet_url = (
        f"https://github.com/pglet/pglet/releases/download/v{version}/{file_name}"
    )
    print(f"Downloading {pglet_url}...")
    urllib.request.urlretrieve(pglet_url, dest_file)
    st = os.stat(dest_file)
    os.chmod(dest_file, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)


def read_chunks(file, size=io.DEFAULT_BUFFER_SIZE):
    """Yield pieces of data from a file-like object until EOF."""
    while True:
        chunk = file.read(size)
        if not chunk:
            break
        yield chunk


def rehash(path, blocksize=1 << 20):
    """Return (hash, length) for path using hashlib.sha256()"""
    h = hashlib.sha256()
    length = 0
    with open(path, "rb") as f:
        for block in read_chunks(f, size=blocksize):
            length += len(block)
            h.update(block)
    digest = "sha256=" + urlsafe_b64encode(h.digest()).decode("latin1").rstrip("=")
    # unicode/str python2 issues
    return (digest, str(length))  # type: ignore


if len(sys.argv) < 3:
    print("usage build-wheels.py <package-version> <pglet-version>")
    sys.exit(1)

package_version = sys.argv[1]
pglet_version = sys.argv[2]
current_dir = pathlib.Path(os.getcwd())
print("package_version", package_version)
print("pglet_version", pglet_version)
print("current_dir", current_dir)

for name, package in packages.items():
    print(f"Building {name}...")

    print("Unpacking original wheel file...")
    orig_whl = current_dir.joinpath("dist", f"pglet-{package_version}-py3-none-any.whl")
    unpacked_whl = current_dir.joinpath("dist", "wheel")
    unpacked_whl.mkdir(exist_ok=True)
    unpack_zip(orig_whl, unpacked_whl)

    # read original WHEEL file omitting tags
    wheel_path = str(
        current_dir.joinpath(
            "dist", "wheel", f"pglet-{package_version}.dist-info", "WHEEL"
        )
    )
    wheel_lines = []

    with open(wheel_path, "r") as f:
        for line in f.readlines():
            if not "Tag: " in line:
                wheel_lines.append(line)

    # print(wheel_lines)

    # read original RECORD file
    record_path = str(
        current_dir.joinpath(
            "dist", "wheel", f"pglet-{package_version}.dist-info", "RECORD"
        )
    )
    record_lines = []

    with open(record_path, "r") as f:
        for line in f.readlines():
            if not "dist-info/WHEEL," in line:
                record_lines.append(line)

    # print(record_lines)

    # create "bin" directory
    bin_path = current_dir.joinpath("dist", "wheel", "pglet", "bin")
    bin_path.mkdir(exist_ok=True)
    asset = package["asset"]
    exec_filename = package["exec"]
    exec_path = str(bin_path.joinpath(exec_filename))
    download_pglet(pglet_version, asset, exec_path)

    # update RECORD
    h, l = rehash(exec_path)
    record_lines.insert(len(record_lines) - 3, f"pglet/bin/{exec_filename},{h},{l}\n")
    # for line in record_lines:
    #     print(line.strip())

    # update WHEEL file
    for tag in package["wheel_tags"]:
        wheel_lines.append(f"Tag: {tag}\n")

    # save WHEEL
    with open(wheel_path, "w") as f:
        f.writelines(wheel_lines)

    # update RECORD
    h, l = rehash(wheel_path)
    record_lines.insert(
        len(record_lines) - 3,
        f"pglet-{package_version}.dist-info/WHEEL,{h},{l}\n",
    )

    # save RECORD
    with open(record_path, "w") as f:
        f.writelines(record_lines)

    # zip
    suffix = package["file_suffix"]
    zip_filename = current_dir.joinpath("dist", f"pglet-{package_version}-{suffix}")
    shutil.make_archive(zip_filename, "zip", unpacked_whl)
    os.rename(f"{zip_filename}.zip", f"{zip_filename}.whl")

    # cleanup
    shutil.rmtree(str(unpacked_whl))

# delete original .whl
os.remove(str(orig_whl))
