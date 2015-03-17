use strict;
use warnings;

my ($IN, %hash, $line, @sorted, $key);

# open test data
chdir("data-files");
open($IN, "<", "codes.txt") or die "can't open input file";


# put data into a hash
foreach $line (<$IN>) {
  $line =~ /^([^\s]+)\s+(.+)$/;
  $hash{$2} = $1;
}

# sort the keys
@sorted = sort keys(%hash);

# print sorted hash
foreach $key (@sorted) {
  print "$key $hash{$key}\n";
}

# lookup Ohio
print "$hash{'Ohio'}\n";


1