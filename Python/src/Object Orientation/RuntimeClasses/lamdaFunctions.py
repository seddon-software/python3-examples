import new

########################################
# define class
myClass_name = 'myClass'
myClass_def = """class %s:
    pass
"""
exec myClass_def % myClass_name

########################################
# define method
function_name = "f"
function_def = """def %s(self):
    print "This is %s()"
"""
exec function_def % (function_name, function_name)

########################################
# create instance
instance = eval(myClass_name)()

########################################
# bind methods
instance.f = new.instancemethod(f, instance, instance.__class__)

lambda_def = eval("lambda self, x: x**2")
instance.g = new.instancemethod(lambda_def, instance, instance.__class__)

########################################
# invoke methods
instance.f()
n = instance.g(30)
print n


1
