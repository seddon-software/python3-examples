############################################################
#
#	Tied Variables
#
############################################################


package TiedArray;
use Tie::Array;
@ISA='Tie::StdArray';

##########
# This tie restricts access to the array to indices in the
# range 2 to 8
##########

$min = 2;
$max = 8;

sub FETCH {
  my($this, $index) = @_;
  if(CheckIndex($index)) { return $$this[$index]; }
  return 0;
}

sub STORE {
  my ($this, $index, $value) = @_;
  if (CheckIndex($index)) { $$this[$index] = $value; }
}

sub CheckIndex {
  ($index) = @_;

  if($index < $min) {
    print "Index $index too small \n";
    return 0;
  }

  if($index > $max) {
    print "Index $index too big \n";
    return 0;
  }

  return 1;
}

############################################################

package main;

tie my @array, 'TiedArray';

print "Set up array ... \n";
foreach $i (0 .. 10) {
  $array[$i] = $i * 100;
}

print "\nRead from array ... \n";
foreach $i (0 .. 10) {
  print "$i: $array[$i] \n";
}
