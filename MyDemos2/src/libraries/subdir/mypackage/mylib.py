class MyClass:
    def f1(self):
        print "f1"
    def f2(self):
        print "f2"
    def f3(self):
        print "f3"
    def f4(self):
        print "f4"

def g1():
    print "g1"
def g2():
    print "g2"
def g3():
    print "g3"
def g4():
    print "g4"
    
# test code follows
def main():
    m = MyClass()
    m.f1()
    m.f2()
    m.f3()
    m.f4()
    g1()
    g2()
    g3()
    g4()

if __name__ == '__main__':
    main()
