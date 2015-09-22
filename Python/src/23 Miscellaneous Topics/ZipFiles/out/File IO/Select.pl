##########################################################
#
#   FileHandles.pl
#
##########################################################

use strict;

my ($OUT1, $OUT2, $OUT3);

chdir("data");
open($OUT1, ">", "data1.txt") || die "Can't open data1.txt";
open($OUT2, ">", "data2.txt") || die "Can't open data2.txt";
open($OUT3, ">", "data3.txt") || die "Can't open data3.txt";

select $OUT2;
print "AAAAAAAAAAAAAAAA";

select $OUT1;
print "BBBBBBBBBBBBBBBB";

select $OUT3;
print "CCCCCCCCCCCCCCCC";

select STDOUT;
print "DDDDDDDDDDDDDDDD";

close($OUT1);
close($OUT2);
close($OUT3);


1

