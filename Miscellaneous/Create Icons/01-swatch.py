import png

size = 3

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

p = []
for i in range(size):
    n = size/3
    if i <= n: p.append(red)
    if i > n and i < 2*n: p.append(green)
    if i >= 2*n: p.append(blue)
print p
fileName = "swatch" + str(size) + ".png"
f = open(fileName, 'wb')
w = png.Writer(size, size)
w.write(f, p) ; f.close()