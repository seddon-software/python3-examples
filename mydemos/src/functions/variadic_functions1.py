def average(*args):
    return sum(args) / len(args)

print( average(4, 6, 9))
print( average(4, 6, 9, 20, 10))
t = (4, 6, 9, 20, 10)
print( average(*t) )