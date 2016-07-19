def square(x):
    print("original")
    return x**2

f = square

def square(x):
    print("new")
    return x * x

x = f(9)
print(x)
square = 'Hello'
print(square)

