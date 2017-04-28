def Fibonacci():
    x = 0
    y = 1
    while x < 100:
        x, y = y, x + y
        yield x     # maps to return statement in iterator
    return          # maps to StopIteration statement in iterator

f = Fibonacci()

for n in f:
    print(n)




    