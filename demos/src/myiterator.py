class Fibonacci:
    def __init__(self):
        self.x = 0
        self.y = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.x, self.y = self.y, self.x + self.y
        if self.x > 100: raise StopIteration()
        return self.x

f = Fibonacci()
print(f.__next__())
print(f.__next__())
print(next(f))

for n in Fibonacci():
    # call __iter__ once
    # call __next__ repeatedly
    print(n)
    
