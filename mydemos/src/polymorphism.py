class Person:
    def eat(self): print("MacDonalds")
    def drink(self): print("Beer")
    def sleep(self): print("ZZZZZZZZZ")

class Employee(Person):
    def eat(self): print("Burger King")
    def drink(self): print("Wine")

class SalesPerson(Employee):
    def eat(self): print("Fat Duck")
    def drink(self): print("Champagne")

class Manager(Person):
    def eat(self): print("Reeds")
    def drink(self): print("Rainwater")
    def sleep(self): print("no sleep")
    
def nightOut(p):
    p.drink()
    p.drink()
    p.eat()
    p.drink()
    p.sleep()
    
def main():
    p = Person()
    e = Employee()
    s = SalesPerson()
    nightOut(p)
    nightOut(e)
    nightOut(s)
    d = Duck()
    nightOut(d)
main()
