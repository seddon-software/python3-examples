$x = 100;
$ptr = \$x;

# point at first function
$subRef = \&f1;
&$subRef("January");

# point at second function
$subRef = \&f2;
&$subRef("February");

# point at anonomous function
$subRef = sub { print "anon:  $_[0] \n"; };
&$subRef("March");

sub f1
{
	print "f1:  $_[0] \n";
}

sub f2
{
	print "f2:  $_[0] \n";
}



1 