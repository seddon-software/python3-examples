############################################################
#
#    polymorphism
#
############################################################

class Person:
    def Eat(self): print "Person eating"
    def Drink(self): print "Person drinking"
    def Sleep(self): print "Person sleeping"

class Employee(Person):
    def Eat(self): print "Employee eating"
    def Drink(self): print "Employee drinking"
    def Sleep(self): print "Employee sleeping"

class SalesPerson(Employee):
    def Eat(self): print "SalesPerson eating"
    def Drink(self): print "SalesPerson drinking"
    def Sleep(self): print "SalesPerson sleeping"


def GotoSleep(p):
    p.Sleep()

p1 = Person()
p2 = Person()
e1 = Employee()
e2 = Employee()
s1 = SalesPerson()
s2 = SalesPerson()

for item in (p1,p2,e1,e2,s1,s2):
    GotoSleep(item)
    