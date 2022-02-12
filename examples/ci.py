import hashlib
import io
from base64 import urlsafe_b64encode

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


def read_chunks(file, size=io.DEFAULT_BUFFER_SIZE):
    """Yield pieces of data from a file-like object until EOF."""
    while True:
        chunk = file.read(size)
        if not chunk:
            break
        yield chunk


def rehash(path, blocksize=1 << 20):
    # type: (str, int) -> Tuple[str, str]
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


sha, len = rehash(
    "/Users/feodor/Downloads/pglet-0.5.14-py3-none-any/pglet/bin/darwin-amd64/pglet"
)
print(sha, len)
