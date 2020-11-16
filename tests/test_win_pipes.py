import pytest
import time
import struct
import pglet

def test_pglet_exe_path():
    print (pglet.pglet_exe)
    assert pglet.pglet_exe != "", "test failed!"

def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test failed"
	#assert x == y,"test failed"
    
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed"

def named_pipe_test():
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