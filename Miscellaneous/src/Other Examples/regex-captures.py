############################################################
#
#    Regular Expressions (pattern capture)
#
############################################################



import re

# myPattern defines 8 groups
myPattern = r"(((\D+)(\d+))((\D+)(\d+))(\D+))"

myCompiledPattern = re.compile(myPattern)
myString = "AAAA1111BBBB2222CCCC"

myMatcher = myCompiledPattern.search(myString)

# print out all group captures
list = myMatcher.groups()

for item in myMatcher.groups():
    print item

# print individual captures
print myMatcher.group(1)
print myMatcher.group(2)
print myMatcher.group(3)




