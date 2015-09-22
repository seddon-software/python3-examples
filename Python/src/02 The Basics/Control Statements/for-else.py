############################################################
#
#    for-else statements
#
############################################################

for x in (1,2,3,4,5,6):
    print x,
else:
    print "only get here if all iterations succeed ..."


for x in (1,2,3,4,5,6):
    print x,
    if x > 3:
        break
else:
    print "only get here if all iterations succeed ..."




