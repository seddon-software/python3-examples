def remove_duplicates(a, b):
    return [element for element in a if element not in b ]
 
def one():
    class I:
        def __init__(self):
            self.x = 0
        def __iter__(self):
            return self
        def __next__(self):
            self.x += 1
            if self.x > 3:
                raise StopIteration()
            return self.x
    
    print(remove_duplicates(dir(I),dir(object)))
    for n in I():
        print(n)

def two():
    class G:
        def gen(self):
            yield 1
            yield 2
            yield 3
            return

    g = G()
    x = g.gen()
    print(type(g.gen()))
    print(remove_duplicates(dir(g.gen()),dir(object)))
    for n in g.gen():
        print(n)

one()
two()
