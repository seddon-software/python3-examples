##########################################################
#
#	Handling Errors
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
  handleError() if ($@);
  print "Loop round again ... \n\n"
}


sub handleError {
  if ($y == 0) { 
    print "Division by zero\n"; 
  } else { 
    print "$@"; 
  }
}
