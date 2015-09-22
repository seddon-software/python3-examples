##########################################################
#
#	Numerical Sort
#
##########################################################

@numbers = (8, 5, 7, 2, 11, 4, 10);
#@sorted = sort numerical @numbers;
@sorted = sort { $a <=> $b } @numbers;
#@sorted = sort @numbers;
print "@sorted";


##########################################################

sub numerical {
    return +1 if($a >  $b);
    return  0 if($a == $b);
    return -1 if($a <  $b);
}
