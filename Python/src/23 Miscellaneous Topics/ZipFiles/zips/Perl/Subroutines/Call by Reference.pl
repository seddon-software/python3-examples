############################################################
#
#        Call by Reference
#
############################################################

my $x = 100;

print "\$x = $x \n";
DoubleIt($x);
print "\$x = $x \n";
DontDoubleIt($x);
print "\$x = $x \n";
DoubleIt2($x);
print "\$x = $x \n";

1;



sub DoubleIt
{
    $_[0] *= 2;
}

sub DontDoubleIt
{
    my ($a) = @_;
    $a *= 2;
    1;
}

sub DoubleIt2
{
	*array = *_;		# use a typeglob to alias _ as array
    $array[0] *= 2;
}

