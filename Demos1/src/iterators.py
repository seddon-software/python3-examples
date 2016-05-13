class MyIterator:
    def __init__(self):
        self.x = 0
        self.y = 1
    
    def __iter__(self):
        return self
    
    def next(self): 
        self.x, self.y = self.x + self.y, self.x
        if self.x > 100: raise StopIteration()
        return self.x

for x in MyIterator():
    print x,

    
