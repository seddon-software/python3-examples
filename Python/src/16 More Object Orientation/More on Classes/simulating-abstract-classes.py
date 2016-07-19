class MyAbstractClass:
    def method1(self): abstract
    def method2(self): abstract
    def method3(self): 
        print "This method is implemented"

class MyClass(MyAbstractClass): 
    # class should implement method1 and method2
    def method1(self):
        print "method1"

# call methods
MyClass().method1()
MyClass().method3()

# failure to implement method2 is detected at run time
MyClass().method2()

1