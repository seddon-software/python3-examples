##########################################################
#
#   Using scratch areas
#
##########################################################


open(IN, "<test.txt");
while(<IN>)
{
  chomp;
  
  split(/:/);      # the scratch array
  print "@_[3,1,2] \n";

  s/:/,/g;        # the scratch scalar
  print;
  print " \n";
}
close(IN);

