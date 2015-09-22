##########################################################
#
#	Catching Errors
#
##########################################################


while(1) {
  eval {
    print "Enter first integer: ";
    chomp($x = <STDIN>);
    print "Enter second integer: ";
    chomp($y = <STDIN>);

    $result = $x / $y;
    print "$x / $y = $result \n";
  };
  print $@;		# print error message
  print "Loop round again ... \n\n"
}

