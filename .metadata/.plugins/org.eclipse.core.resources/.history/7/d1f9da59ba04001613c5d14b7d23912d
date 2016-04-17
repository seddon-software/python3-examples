from timeit import Timer, timeit
class Timing:
    print "{:20s}{:>8s}{:>8s}{:>8s}".format("code", "repeats", "time", "1/time")
    print "{:20s}{:>8s}{:>8s}{:>8s}".format("====", "=======", "====", "======")
    
    def __init__(self, method):
        n = 10 * 1000 * 1000
        self.method = method
        name = method.__name__
        timer = Timer(stmt='{}({})'.format(name, n),setup='from __main__ import {}'.format(name))
        result = timer.timeit(number=1)
        print "{:20s}{:8d}{:8.3f}{:8.3f}".format(name, n, result, 1/result)

###################################################################################################

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        self.x += 1
        self.y += 1

#define functions to time
def fragment1(n):
    p = Point(0, 0)
    for i in range(n):
        p.move()

def fragment2(n):
    for i in range(n):
        p = Point(0, 0)
        p.move()

def fragment3(n):
    for i in range(n):
        p = Point(0, 0)
        p.move()
        del p

def fragment4(n):
    l = []
    for i in range(n/2):
        l.append(Point(0, 0))
    for i in l:
        i.move()



Timing(fragment1)
Timing(fragment2)
Timing(fragment3)
Timing(fragment4)
