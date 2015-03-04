##########################################################
#
#	Write locks (test with ReadLock.pl)
#
##########################################################

use strict;

my $LOCK_SHARED      = 1;
my $LOCK_EXCLUSIVE   = 2;
my $LOCK_NONBLOCKING = 4;
my $UNLOCK           = 8;

open(my $DB, ">", "data/testdata.txt") || die "Can't open testdata.txt";
flock($DB, $LOCK_EXCLUSIVE);

print "File locked for writing ...\n";
print($DB "This is line 1.\n");
print($DB "This is line 2.\n");
sleep 10;
print($DB "This is line 3.\n");
print($DB "This is line 4.\n");

flock($DB, $UNLOCK);
print "File unlocked ...\n";

close($DB);


