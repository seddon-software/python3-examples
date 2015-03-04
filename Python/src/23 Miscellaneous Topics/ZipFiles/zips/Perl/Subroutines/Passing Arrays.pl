############################################################
#
#        Call by Reference
#
############################################################

my @array = (30 .. 39);

DoubleIt(@array);
print "\@array = @array \n";

1;



sub DoubleIt
{
    foreach my $item (@_) {
    	$item *= 2;
    	1;
    }
}

sub DoubleIt2
{
	*array = *_;		# use a typeglob to alias _ as array
    $array[0] *= 2;
}

