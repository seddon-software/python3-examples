x = 240
print("{address:8X}, {var:06d}".format(address=id(x), var=x))
x = x + 16
print("{:8X}".format(id(x)))
