############################################################
#
#        Exercise 1
#
#		 Splice in zeros to an array between start and end indeces
#
############################################################

my @data = (5, 8, 10, 6, 3, 4, 7, 2);
my ($start, $end) = (2, 4);

@result = Modify($start, $end, @data);
print "@data \n";
print "@result \n";

sub Modify {
    my ($start, $end, @data) = @_;
	my @insert = Zero($end - $start + 1);    
    splice(@data, $start, $end, @insert);
    return @data;
}

sub Zero {
	my ($size) = @_;
	my @array = ();
	$#array = $size - 1;
    for $item (@array)
    {
    	$item = 0;
    	1;
    }
	return @array;
}