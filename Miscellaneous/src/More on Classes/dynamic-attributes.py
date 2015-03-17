############################################################
#
#    dynamic-attributes
#
############################################################

# create an empty class
class Person:
    pass



# dynamically add attributes
john = Person()
john.name = "John Smith"
john.age = 27
john.nationality = "British"
print john.__dict__

sheila = Person()
sheila.name = "Sheila Lawry"
sheila.age = 32
sheila.nationality = "Australian"
sheila.height = 1.87
sheila.weight = 139
print sheila.__dict__

# read in a method into a string
getDetailsMethod = """
def getDetails(self):
    print self.name, " age", self.age, " nationality", self.nationality
"""

# execute the code fragment at runtime to create a method
exec getDetailsMethod

# add it to the class
setattr(Person,"getDetails",getDetails)

# invoke dynamically generated method
john.getDetails()
sheila.getDetails()
print Person.__dict__