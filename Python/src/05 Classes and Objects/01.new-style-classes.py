class Person(object):
    age = 15
    def __init__(self, name):
        self.Print()
        self.name = name
        self.Print()
        Person.age = self.age + 1
        self.Print()
        self.age = self.age + 1
        self.Print()
        1

    def Eat(self): pass        
    def Drink(self): pass        
    def Sleep(self): pass        
    def Print(self):
        print self.__dict__
        print self.__class__.__dict__

p = Person("Anne")
print p.age
print p.__dict__["age"]
print Person.age
print Person.__dict__["age"]
print p.__class__.__dict__["age"]

p.Eat()
p.Drink()
p.Sleep()
p.Print()

q = Person("Fred")
q.Print()
1