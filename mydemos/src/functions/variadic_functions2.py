def volume(**h):
    return h['height'] * (h['width'] + 2) * (h['depth'] + 5)

print( volume(height=10, width=8, depth=6))
print( volume(width=8, depth=6, height=10))
d = { 'width' : 8, 'depth' : 6, 'height' : 10 }
print( volume(**d) )
