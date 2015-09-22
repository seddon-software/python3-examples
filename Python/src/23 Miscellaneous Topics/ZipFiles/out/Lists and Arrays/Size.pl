##########################################################
#
#	Size of an Array
#
##########################################################

use strict;

my @array = (27 .. 99, 0 .. 26);

# copy the array
my @copy = @array;
 
# find the size of an array (using scalar context)
my $size;
$size = @array;			# implicit context
$size = scalar(@array); # explicit context

print $size;

1;