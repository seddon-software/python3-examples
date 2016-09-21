def volume(**kwargs):
    defaults = { 'length' : 1, 'width' : 1, 'height' : 1 }
    defaults.update(kwargs)
    kwargs = defaults
    return kwargs['length'] * (kwargs['width'] + 2) * (kwargs['height'] + 5)

print( volume())
print(volume(width=12, height=14))
print(volume(height=14, length=10, width=12))
d = { 'height':14, 'length':10, 'xxxwidth':12 }
print(volume(**d))
