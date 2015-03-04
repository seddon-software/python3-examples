############################################################
#
#    generators
#
############################################################

# generators are a shortcut to building iterators

# class is not iterable in sense that 
#    the class doesn't define __iter__() and next()
# but any method that contains yield 
#    will be converted to an iterator internally
class Fibonacci:
    def __init__(self):
        self.x,self.y = 0,1
        
    def myGenerator(self):
        while self.x < 100:
            yield self.x    # suspends execution and returns
            self.x, self.y = self.y, self.x + self.y
        return  # no more yields left

f = Fibonacci()             # create object
iter = f.myGenerator()      # call generator function to create an iterable

for n in iter:              # invoke the iterable
    print n,

for n in Fibonacci().myGenerator():              # invoke the iterable
    print n,








1