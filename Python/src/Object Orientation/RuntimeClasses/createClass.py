myClass_name = 'myClass'
myClass_def = """class %s:
    pass
"""
code = myClass_def % myClass_name
print code
exec myClass_def % myClass_name

x1 = myClass()

instance = eval(myClass_name)()

1
