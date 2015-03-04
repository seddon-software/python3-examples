##################################################
#
#     array references
#
##################################################

@array = ('Tom', 'Ali', 'Mary');
$arrayRef = \@array;

print "$$arrayRef[0] \n";
print "$$arrayRef[1] \n";
print "$$arrayRef[2] \n";

print "---- \n";

print "$arrayRef->[0] \n";
print "$arrayRef->[1] \n";
print "$arrayRef->[2] \n";

1