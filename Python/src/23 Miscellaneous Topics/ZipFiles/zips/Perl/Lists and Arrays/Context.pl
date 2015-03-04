##########################################################
#
#	Scalar Context
#
##########################################################

@array = (5 .. 15);
print "Original: @array \n";

$n = @array;
@x = @array;

print "Scalar: $n \n";
print "List:   @x \n";
