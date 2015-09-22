##########################################################
#
#	sprintf
#
##########################################################


$x1 = 163.58352;
$x2 = 23.857179;

$message = sprintf("Numbers are %.2f and %.2f \n", $x1, $x2);
Print_3_Times($message);
1;

sub Print_3_Times() {
  print @_;
  print @_;
  print @_;
}

