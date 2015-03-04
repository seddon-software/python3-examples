import random, time

count = 0

def f1():
    global count
    for i in xrange(10000):
        time.sleep(random.random() * 0.001)
        count = count + i

def f2():
    global count
    for i in xrange(20000):
        time.sleep(random.random() * 0.001)
        count = count + i

def f3():
    global count
    for i in xrange(30000):
        time.sleep(random.random() * 0.001)
        count = count + i

def f4():
    global count
    for i in xrange(40000):
        time.sleep(random.random() * 0.001)
        count = count + i


def foo():
    f1()
    f2()
    f3()
    f4()
    
