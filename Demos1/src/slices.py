p = range(20, 40)
q = p[:]  # shallow copy
r = p
print id(p)
print id(q)
print id(r)

