############################################################
#
#        Passing Scalars
#
############################################################

$result = Average(10, 15);        print "$result \n";
$result = Average(12, 16);        print "$result \n";
$result = Average(14, 17);        print "$result \n";
$result = Average(16, 18);        print "$result \n";
1;

sub Average
{
  my ($x, $y) = @_;        # Locals
  return ($x + $y)/2.0;
}
