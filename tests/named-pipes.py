import time
import struct
import os

pipe_name = "/tmp/pglet_pipe_dpk1hyym6e"

#wf = os.open(rf'{pipe_name}', os.O_SYNC | os.O_RDWR)
#os.write(wf, b'clean page')

f = open(rf'{pipe_name}', "w")

f.write('clean page')
f.close()

f = open(rf'{pipe_name}', "r")
r = f.readline()

print(r)