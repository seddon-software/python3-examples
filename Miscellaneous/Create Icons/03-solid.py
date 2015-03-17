import png
from numpy import *

size = 32


def f(x,y):
    for i in nditer(y, op_flags=['readwrite']):
        print i,
        i[...] = i % 3
    result = (x + y * 100) % 256
    return result


p = fromfunction(f, (size, 3 * size), dtype = int)

fileName = "colors" + str(size) + ".png"
f = open(fileName, 'wb')
w = png.Writer(size, size)
w.write(f, p)
f.close()