##########################################################
#
#	times()
#
##########################################################



use Time::Local;

print "Gathering statistics ... \n";

for($i = 0; $i < 1000; $i++) {
  $x = `dir`;
}


$realTime = times();
@allTimes = times();
($user, $system, $childUser, $childSystem) = times();

print "Array:  @allTimes \n";
print "Scalar: $realTime \n";
print "List:   $user $system \n";
