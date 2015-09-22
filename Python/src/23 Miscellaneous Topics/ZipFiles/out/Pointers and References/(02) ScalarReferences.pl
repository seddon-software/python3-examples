############################################################
#
#	Scalar References
#
############################################################

my $x = 100;
my $xref = \$x;		# xref is an alias for x

$x++;				# increments x and xref
print "x = $x, xref = $$xref \n";

$$xref++;			# increments xref and x
print "x = $x, xref = $$xref \n";



1
