############################################################
#
#	Typeglobs
#
############################################################

# you can define different scalars, arrays and hashes 
#  all with the same name

$x = 100;
@x = (20 .. 30);
%x = ('a' => 65, 'b' => 66);

print "$x \n";
print "$x[3] \n";
print "$x{'b'} \n";

# use a typeglob to set an alias y for x
*y = *x;		# aliases scalar, array and hash

print "$y \n";
print "$y[3] \n";
print "$y{'b'} \n";


1
