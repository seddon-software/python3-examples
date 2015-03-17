##########################################################
#
#	Slurping
#
##########################################################

use strict;
use English;
use File::Slurp;

our $IN;

chdir("data");
open($IN,  "<", "testdata.txt") || die "Can't open testdata.txt";

slurpingIntoAScalar();
slurpingIntoAnArray();
slurpingUsingSlurpModule();

close($IN);


#######################################################

sub slurpingIntoAScalar
{
	# reset the file position to start of file
	seek($IN, 0, 0);

	# use local to shadow the existing record separator and make it undef
	# don't use "my" or the shadow will not apply to readline called from <$IN>
	# if there is no line separator one scalar read will slurp the whole file
	my $lines = do { local $INPUT_RECORD_SEPARATOR ; <$IN>};
	1;
}

sub slurpingIntoAnArray
{
	# reset the file position to start of file
	seek($IN, 0, 0);

	# read line by line into an array
	my @myLines = <$IN>;
	1;
}

sub slurpingUsingSlurpModule
{	
	# slurp into scalar
	seek($IN, 0, 0);
	my $lines = File::Slurp::slurp($IN);
	
	# slurp into array
	seek($IN, 0, 0);
	my @lines = File::Slurp::slurp($IN);

	1;
}

1