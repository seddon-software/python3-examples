##########################################################
#
#	Directories
#
##########################################################

use strict;
my $DIR;

opendir($DIR, "data");
my @files = readdir($DIR);
print("FILES: @files \n");
close($DIR);


my $NotADotFile = "^[^\.]";

foreach my $file (grep /$NotADotFile/,@files)
{
  print "$file \n";
}


1

