def g(fn, n):
    return fn(n)

def square(n):
    return n * n

# def cube(n):
#     return n**3
cube = lambda n : n**3

print g(cube, 3)
print g(square, 5)
print g(lambda x : 2 * x, 17)