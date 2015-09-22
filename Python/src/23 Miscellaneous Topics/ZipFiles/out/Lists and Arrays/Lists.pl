##########################################################
#
#	Lists
#
##########################################################

use strict;
my ($IN, $line, $FirstName, $LastName, $PhoneNumber);

open($IN, "<", "Phones.txt");

while($line = <$IN>) {
  ($FirstName, $LastName, $PhoneNumber) = 
     split('\s+', $line);
  print "$LastName \n";
}

close($IN);
