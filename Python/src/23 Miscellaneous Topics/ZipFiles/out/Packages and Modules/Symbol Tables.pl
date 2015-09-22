##########################################################
#
#	
#
##########################################################



package PackageA;

our $x = 100;		# global
my  $y = 101;		# local
sub Sub1 { print "This is function 1 \n"; }
sub Sub2 { print "This is function 2 \n"; }
sub Sub3 { print "This is function 3 \n"; }

############################################################

package PackageB;

our $x = 200;		# global
my  $y = 201;		# local
sub Sub1 { print "This is subroutine 1 \n"; }
sub Sub2 { print "This is subroutine 2 \n"; }
sub Sub3 { print "This is subroutine 3 \n"; }

############################################################

package main;

sub DisplayHash($);

our $x = 300;		# global
my  $y = 301;		# local

print $PackageA::x,"\n";
print $PackageA::y,"\n";
print $PackageB::x,"\n";
print $PackageB::y,"\n";
print $main::x,"\n";
print $::x,"\n";

print "===== PackageA ===== \n";
DisplayHash(\%PackageA::);
print "===== PackageB ===== \n";
DisplayHash(\%PackageB::);
print "===== main ===== \n";
DisplayHash(\%main::);

1;

sub DisplayHash($) {
	my ($rhash) = @_;
	%hash = %$rhash;
	 
	foreach $key (keys(%hash)) {
		printf "%-16s%-16s\n", $key, $hash{$key};
		1;
	}
}

