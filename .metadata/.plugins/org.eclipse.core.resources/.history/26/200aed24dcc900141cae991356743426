##########################################################
#
#	Copy program
#
##########################################################

use strict;
my ($IN, $OUT);

chdir("data");
open($IN,  "<", "testdata.txt") || die "Can't open testdata.txt";
open($OUT, ">", "results.txt")  || die "Can't open results.txt";

my @allLines = <$IN>;
foreach my $line (@allLines)
{
	print $line;
}

while (my $line = <$IN>) {
  print {$OUT} "$.: " . $line;
  print        "$.: " . $line;
}

close($IN);
close($OUT);


1