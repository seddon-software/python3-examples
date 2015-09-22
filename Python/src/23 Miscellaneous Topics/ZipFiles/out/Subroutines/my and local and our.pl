############################################################
#
#        my and local
#
############################################################

use strict;
our $x = "Global";
our $y = "Global";
print "main:     \$x = $x ... \$y = $y \n";
routineA();
print "main:     \$x = $x ... \$y = $y \n";

sub routineA {
  local $x = "Local ";
  my    $y = "My    ";
  print "routineA: \$x = $x ... \$y = $y \n";
  routineB();
}

sub routineB {
  print "routineB: \$x = $x ... \$y = $y \n";
  routineC();
}

sub routineC {
  print "routineC: \$x = $x ... \$y = $y \n";
}
1
