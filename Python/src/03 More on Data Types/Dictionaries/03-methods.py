############################################################
#
#    dictionary
#
############################################################

# set up a dictionary
salary = {
 		  "zak":   34000, 
          "sara":  27000,
          "pedro": 52000,
          "kilas": 12500,
          "zoe":   66000
         }
salary["sara"] = 28000
salary["sara"] = None
salary["george"] = 137000

# delete keys using del and pop
del salary["zak"]
value = salary.pop("kilas")

# read and write
salary["pedro"] = 53000
print salary["pedro"]

# print all the keys
for key in salary.iterkeys():
    print key,
print

# print all the values
for value in salary.itervalues():
    print value,
print

# print all <key,value> pairs
for key, value in salary.iteritems():
    print key, value

# check if key in dictionary
if salary.has_key("george"): print "george is in dictionary"

if "sara" in salary: print "sara is in dictionary"

1
