def memoize(f):
    cache = {}
    def inner(n):
        # print("{}: {}".format(n, cache))
        if n in cache:
            return cache[n]
        else:
            cache[n] = f(n)
            return cache[n]
    return inner

@memoize
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

print( fib(8) )
