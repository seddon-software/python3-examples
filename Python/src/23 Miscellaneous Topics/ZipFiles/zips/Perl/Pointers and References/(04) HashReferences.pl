##################################################
#
#     hash references
#
##################################################

%hash = ('Tom'  => 539, 
		 'Ali'  => 377, 
		 'Mary' => 470 );
$hashRef = \%hash;

print "$$hashRef{'Tom'} \n";
print "$$hashRef{'Ali'} \n";
print "$$hashRef{'Mary'} \n";

print "---- \n";

print "$hashRef->{'Tom'} \n";
print "$hashRef->{'Ali'} \n";
print "$hashRef->{'Mary'} \n";


1