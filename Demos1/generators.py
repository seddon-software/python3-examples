def fib():
    x = 0
    y = 1
    
    while(x < 100):
        x, y = x + y, x
        yield y  # return of the iterator
        x = x + 0
    return       # StopIteration of the iterator

for x in fib():
    print x,
    
