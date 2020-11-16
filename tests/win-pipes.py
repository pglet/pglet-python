import time
import struct

pipe_name = "pglet_pipe_7jbngddx9s"

f = open(rf'\\.\pipe\{pipe_name}', 'r+b', buffering=0)

f.write(b'clean page')
r = f.readline()

f.write(b'add text value="Hello, world!"')
r = f.readline()

f.write(b'add text value="Line 2"')
r = f.readline()

f.write(b'add button id="ok" text="OK"')
r = f.readline()

f = open(rf'\\.\pipe\{pipe_name}.events', 'r+b', buffering=0)
r = f.readline()

print(r)