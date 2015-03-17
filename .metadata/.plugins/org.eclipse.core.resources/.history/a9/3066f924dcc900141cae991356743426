use strict;
use warnings;


my $myString1 = <<"HERE_DOC";
This is a 
multi line string
embedded in
a here document.
HERE_DOC

my $myString2 = "This is a\n"
              . "multi line string\n"
              . "that gets concatenated\n"
              . "together.\n";
           
print "$myString1";
print "$myString2";
print build_string("Goodbye", "Universe");

#######################################################

sub build_string {
	my ($parameter_1, $parameter_2) = @_;
	return <<"HERE_DOC";
This is a multi line string
with embedded parameters
$parameter_1 ans $parameter_2
all enclosed in a here document.
HERE_DOC
}

1