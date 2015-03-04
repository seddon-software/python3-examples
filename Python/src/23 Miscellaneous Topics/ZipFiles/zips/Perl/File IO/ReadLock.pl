##########################################################
#
#	Read locks (test with WriteLock.pl)
#
##########################################################

use strict;

my $LOCK_SHARED      = 1;
my $LOCK_EXCLUSIVE   = 2;
my $LOCK_NONBLOCKING = 4;
my $UNLOCK           = 8;

open(my $DB, "data/testdata.txt") || die "Can't open testdata.txt";
flock($DB, $LOCK_SHARED);

print "File locked for reading ...\n";
$_ = <$DB>; print;
$_ = <$DB>; print;
sleep 10;
$_ = <$DB>; print;
$_ = <$DB>; print;
flock($DB, $UNLOCK);
print "File unlocked ...\n";

close($DB);


1