import png

size = 120

def getRow(r,g,b):
    pattern = []
    for i in range(size):
        pattern.append(r)
        pattern.append(g)
        pattern.append(b)
    return pattern
    
red = getRow(255,0,0)
green = getRow(0,255,0)
blue = getRow(0,0,255)

r = 120
g = 140
b = 160
p = []
for i in range(size):
    pattern = []
    for j in range(size):
        pattern.append((r+i+j)%256)
        pattern.append((g+i+j)%256)
        pattern.append((b+i+j)%256)
    p.append(pattern)
print p
fileName = "z" + str(size) + ".png"
f = open(fileName, 'wb')
w = png.Writer(size, size)
w.write(f, p) ; f.close()