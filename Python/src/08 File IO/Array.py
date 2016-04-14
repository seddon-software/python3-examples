############################################################
#
#    array
#
############################################################

import array

f = open("data/mytest1.bin", "w")
a = array.array('c', ['A']*100)
a.extend(['1'] * 100)
b = array.array('c', ['B']*100)
a.extend(b)
a.tofile(f)
f.close()

import subprocess
subprocess.call("hexdump -x data/mytest1.bin".split())
1