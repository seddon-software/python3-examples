class Foo:
    def bar (self):
        print "Hello from original method", self
instancemethod = type (Foo.bar)
foo_obj = Foo ()
# Implement a new method
def my_new_method (self):
    print "Hello from my_new_method of object", self
def another_method (self):
    print "Hello from another_method of object", self
# Keep the old method just for fun
old_method = foo_obj.bar
# Define the new method bound to an object
foo_obj.bar = instancemethod (my_new_method, foo_obj, Foo)
# Define a new method bound to a class
old_foo_obj = Foo ()
Foo.bar = instancemethod (another_method, None, Foo)
new_foo_obj = Foo ()
# Original method will be called
old_method ()
# We redefined the method, it will be called
foo_obj.bar ()
# We didn't redefined the method of these instances, thus the class definition
# will be used
new_foo_obj.bar ()
old_foo_obj.bar ()
