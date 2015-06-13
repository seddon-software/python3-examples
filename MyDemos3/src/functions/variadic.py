def f(*args, **kwargs):
    for p in args:
        print p,
    print
    
    for (key, value) in kwargs.iteritems():
        print key, value 

# f(3, 5, 7, 9, 11)
# f(2, 4, 8)
# f(a = 4, b = 6)
mytuple = (7, 9, 11)
myhash = { 'a' : 4, 'b' : 6 }
f(3, 5, *mytuple, **myhash)
