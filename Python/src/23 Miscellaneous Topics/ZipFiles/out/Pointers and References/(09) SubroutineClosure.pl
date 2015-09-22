#######################################################
#
#	subroutine closure
#
#######################################################

# define a subroutine with a context that returns
#  another a pointer to another subroutine
 
sub f
{
	# define a local context
	my $firstName = "John";
	my $lastName = "Doe";
	
	# the anonomous subroutine inherits the context
	my $ptr = sub 
	{
		print "@_ \n";
		print $firstName, $lastName
		
	};
	
	# return pointer to subroutine
	return $ptr; 
}

# call function that returns a function with context
$fp = f();

# invoke the new function
#  the function knows about parameters
#  but also knows about its parents context
&$fp(20 .. 25);




1



