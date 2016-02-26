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
        
    def myGeneratorFunction(self):
        while self.x < 100:
            yield self.x    # suspends execution and returns
            self.x, self.y = self.y, self.x + self.y
        return  # no more yields left

f = Fibonacci()             # create object
gen_iter = f.myGeneratorFunction()      # call generator function to create an iterable

print "Type of gen-iter:", type(gen_iter)
print "Does gen-iter have an '__iter__' function:", hasattr(gen_iter, "__iter__")
print "Does gen-iter have an 'next' function:", hasattr(gen_iter, "next")

for n in gen_iter:   # invoke the iterable
    print n,









1