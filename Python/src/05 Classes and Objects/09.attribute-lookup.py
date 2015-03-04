############################################################
#
#    attribute lookup
#
############################################################

class A(object):
    x = 100

    # used if attribute not found by lookup
    def __getattr__(self, name):
        self.__dict__[name] = 0 # used to avoid recursion
        return self.__dict__[name]

a1 = A()
a1.x = 200

a2 = A()

print a1.x  # attribute found in instance
print a2.x  # attribute found in class
print a2.y  # attribute not found

print a1.__dict__
print a2.__dict__
print A.__dict__




1
