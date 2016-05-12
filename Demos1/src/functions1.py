def square(n):
    return n**2

def cube(n):
    return n**3

# def quad(n):
#     return n**4
quad = lambda n : n**4


def power(fn, n):
    return fn(n)

print power(quad, 10)
print power(lambda n : n**4, 10)
print power(square, 17)

