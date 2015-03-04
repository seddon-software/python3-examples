import new

########################################
# build a runtime class
myClass_name = 'myClass'
myClass_def = """class %s:
    pass
"""
exec myClass_def % myClass_name

########################################
# build a runtime method
function_name = "f"
function_def = """def %s(self):
    print "This is %s()"
"""
exec function_def % (function_name, function_name)

########################################
# create instance of class
instance = eval(myClass_name)()
# bind method to object
instance.f = new.instancemethod(f, instance, instance.__class__)
# call method
instance.f()

1
