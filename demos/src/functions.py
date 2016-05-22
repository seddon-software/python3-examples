def square(n):
    return n**2

def cube(n):
    return n**3

def quad(n):
    return n**4

def power(fn, n):
    return fn(n)
    
print power(cube, 9)

print square(5)
print cube(7)
print quad(9)
