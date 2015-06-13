class Person(object):
    def eat(self): print "MacDonalds"
    def drink(self): print "Beer"
    def sleep(self): print "ZZZZZZZZZZZZZ"
    
class Employee(Person):
    def eat(self): 
        Person.drink(self)
        print "Witherspoons"
    def drink(self): print "Wine"

class SalesPerson(Employee):
    def eat(self): 
        Person.eat(self)
        print "Fat Duck"
    def drink(self): print "Champagne"

class Horse:
    def eat(self): print "Hay"
    def drink(self): print "water"
    def sleep(self): print "ZZZ ZZ  ZZZZZZ ZZZ"
     
p = Person()
e = Employee()
s = SalesPerson()
h = Horse()

import copy
def NightOut(p):
    print '******', p.__class__.__mro__
    p.drink()
    # cast to an Employee
    e = copy.copy(p)
    e.__class__ = Employee
    e.drink()
    
    # call method in superclass 
    if isinstance(p, Employee):
        p.__class__.__bases__[0].drink(e)
    else:
        p.drink()
    p.eat()

NightOut(p)
NightOut(e)
NightOut(s)
#NightOut(h)
