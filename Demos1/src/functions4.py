def volume(**d):
    return d['height'] * (d['width'] + 4) * (d['length'] + 2)

print volume(height=14, width=10, length=12)
print volume(length=12, height=14, width=10)
params = { 'length' : 12, 'height' : 14, 'width' : 10, 'junk' : 99 }
print volume(**params)
