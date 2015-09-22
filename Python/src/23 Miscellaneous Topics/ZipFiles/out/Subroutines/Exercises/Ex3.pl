############################################################
#
#        Exercise 3
#
#		 Sum two array
#
############################################################

my @array1 = (5, 8, 10, 6, 3, 4, 7, 2);
my @array2 = (5, 2,  0, 4, 7, 6, 3, 8);

@result = Sum(@array1, @array2);
print "@result \n";

sub Sum {
	my (@first) = (@_);
	my @second = @first;
	my $size = ($#first + 1) / 2;
	
	for (1 .. $size)
	{
		pop(@first);
		shift(@second);		
	}
	my @result;
	
	for my $i (0 .. $#first) {
		$result[$i] = $first[$i] + $second[$i];
	}
	return @result;
}

