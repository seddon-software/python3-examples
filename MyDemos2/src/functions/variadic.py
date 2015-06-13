def f(*args, **kargs):
    print args
    print kargs
    


t = (7, 2, 43)
h = { 'c' : 3, 'd' : 4 }
f(3, 4, 6, *t, a = 1, b = 2, **h)

