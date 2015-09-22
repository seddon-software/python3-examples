##########################################################
#
#        Splice
#
##########################################################

@original = (10 .. 20);
@insert   = (990 .. 999);
$startAt  = 5;
$remove   = 2;

splice(@original, $startAt, $remove, @insert);
print "@original \n";

1;