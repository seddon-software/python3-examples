##########################################################
#
#	Throwing Errors
#
##########################################################

while (1) {
	eval {
		print "Enter an integer: ";
		chomp( $x = <STDIN> );

		$result = Square($x);
		print "$x * $x = $result \n";
	};
	     print "$@";
	  handleError() if ($@);
	     print "Loop round again ... \n\n";
}

sub Square {
	my ($n) = @_;

	die "Too small" if ( $n < 0 );
	die "Too big"   if ( $n > 10 );

	return $n * $n;
}

sub handleError {
	$error = $@;
	print "Too small\n" if ( $error =~ /Too small/ );
	print "Too big\n"   if ( $error =~ /Too big/ );
}
