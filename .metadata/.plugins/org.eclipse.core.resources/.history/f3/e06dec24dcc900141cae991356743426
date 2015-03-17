############################################################
#
#	Termination
#
############################################################

while(1) {
	print "Enter action code(1-4): ";
	chop($code = <STDIN>);
	f1($code);
}

sub f1
{
	f2($_[0]);
}

sub f2
{
	action($_[0]);
}

####################################

sub action 
{
	use Carp;
	my ($number) = @_;

	if ($number == 1) { die "Code 1 - die "; }
	if ($number == 2) { warn "Code 2 - warn "; }
	if ($number == 3) { carp "Code 3 - carp "; }
	if ($number == 4) { croak "Code 4 - croak "; }

	print "I am not dead! \n"; 
}
