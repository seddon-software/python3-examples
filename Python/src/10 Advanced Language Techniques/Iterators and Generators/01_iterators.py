############################################################
#
#    iterators
#
############################################################

# iterators must support two methods: __iter__ and next

class Fibonacci:
    def __init__(self):
        self.x,self.y = 0,1
        
    def __iter__(self):
        return self  # the object on which to call next() - usually ourself

    def next(self):
        if self.x > 100:
            raise StopIteration     # indicate end of iteration
        
        self.x, self.y = self.y, self.x + self.y
        return self.x

# create an instance of class and invoke iterator methods
# __iter__(self) will be called once
# next(self) will be called until loop terminates
for f in Fibonacci():
    print f,


1







