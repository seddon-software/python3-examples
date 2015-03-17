import png
from numpy import *

size = 32

color = (0, 255, 255)

def f(x,y):
    for i in nditer(y, op_flags=['readwrite']):
        i[...] = color[i % 3]
    return y


p = fromfunction(f, (size, 3 * size), dtype = int)
colorString = "_" + str(color[0]) + "_" + str(color[1]) + "_" + str(color[2]) + "_"
fileName = "rgb" + colorString + str(size) + ".png"
f = open(fileName, 'wb')
w = png.Writer(size, size)
w.write(f, p)
f.close()