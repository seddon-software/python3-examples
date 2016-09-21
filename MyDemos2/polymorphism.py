class Person:
    def eat(self): print("MacDonalds")
    def drink(self): print("Stella")
    def sleep(self): print("ZZZZZZZZZZ")

class Employee(Person):
    def eat(self):
        super(Employee, self).eat()
        Person.eat(self) 
        print("Nandos")
    def drink(self): print("Wine")

class SalesPerson(Employee):
    def eat(self): print("Fat Duck")
    def drink(self): print("Champagne")

class Horse:
    def eat(self): 
        Person.eat(self) 
        print("Hay")
    def drink(self): print("Water")
    def sleep(self): print("Neighhhhh")

def NightOut(p):
    p.drink()
    p.drink()
    p.eat()
    p.drink()
    p.sleep()
    
p = Person()
e = Employee()
s = SalesPerson()
h = Horse()
NightOut(p)
NightOut(e)
NightOut(s)
NightOut(h)


