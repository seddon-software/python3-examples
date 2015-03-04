############################################################
#
#    strings
#
############################################################

s = "---abc:XYZ:123---"
t = s.lower()
t = s.lstrip("-")
t = s.replace(":","@")
t = s.rstrip("-")
t = s.split(":")
t = s.strip("-")
t = s.swapcase()
t = s.upper()

print s.lower()
print s.lstrip("-")
print s.replace(":","@")
print s.rstrip("-")
print s.split(":")
print s.strip("-")
print s.swapcase()
print s.upper()
1