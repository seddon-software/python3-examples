#######################################################
#
#	returning pointers to subroutines
#
#######################################################

sub g
{
	print "g: @_ \n";
}

sub f
{
	print "This is f \n";
	return \&g; 
}

# call function that returns a pointer to subroutine
$fp = f();

# invoke the new subroutine
&$fp(20 .. 25);

1



