
############################################################
#
#    eval operators
#
############################################################

x = 10
y = 20
codeFragment = raw_input("Please enter an expression (e.g. 'x + y'): ")

result = eval(codeFragment.rstrip())
print "result is: ", result

