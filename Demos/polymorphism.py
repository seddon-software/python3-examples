class Person(object):
    def eat(self): print "McDonalds"
    def drink(self): print "Beer"
    def sleep(self): print "ZZZZZZZZZZ"

class Employee(Person):
    def eat(self): print "KFC"
    def drink(self): print "Wine"

class Manager(Employee):
    def eat(self): print "Fat Duck"
    def drink(self): print "Champagne"

class Horse(object):
    def eat(self): print "Hay"
    def drink(self): print "Water"
    def sleep(self): print "Neeeiiiigggghhh"
    
def NightOut(p):
    p.drink()
    p.drink()
    p.eat()
    p.drink()
    p.sleep()
    

h = Horse()
NightOut(h)

p = Person()
e = Employee()
m = Manager()
NightOut(p)
NightOut(e)
NightOut(m)


