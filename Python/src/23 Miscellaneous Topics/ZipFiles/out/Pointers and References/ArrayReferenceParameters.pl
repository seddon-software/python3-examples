##################################################
#
#     array references as parameters
#
##################################################

use strict;


my @arrayA = (10, 17, 13, 15, 12);
my @arrayB = (20, 13, 17, 15, 18);
my @result = Combine(\@arrayA, \@arrayB);
print "@result \n";



sub Combine($$) {
    my ($refA, $refB) = @_;
    my @result;
    
    foreach my $i (0 .. @$refA - 1) {
        $result[$i] = $refA->[$i] + $refB->[$i];
        1;
    }
    return @result;
}

1

