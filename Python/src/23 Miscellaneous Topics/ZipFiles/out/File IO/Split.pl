use strict;
use warnings;

my ($IN, $line, $FirstName, $LastName, $PhoneNumber, $fileName);

$fileName = "data/Phones.txt";
open($IN, "<", $fileName) or die "can't open $fileName";

while($line = <$IN>) {
    ($FirstName, $LastName, $PhoneNumber) = split('\s+', $line);
    print "$LastName \n";
}
close($IN);
