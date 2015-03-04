############################################################
#
#    strings (immutable)
#
############################################################


"""
this
is almost
a multi-line
comment
"""


x = 'hello'
y = "from"
z = '''the
 planet """zzzz
           zzzz"""
 earth'''
 
print type(x)
print x, y, z

phrase = x + " " + y + " " + z
print phrase.upper()