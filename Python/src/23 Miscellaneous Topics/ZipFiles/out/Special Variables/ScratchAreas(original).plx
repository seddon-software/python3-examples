##########################################################
#
#	Using scratch areas
#
##########################################################


open(IN, "<test.txt");
while($_ = <IN>)
{
  chomp $_;
  
  @_ = split(/:/, $_);		# the scratch array
  print "@_[3,1,2] \n";

  $_ =~ s/:/,/g;		# the scratch scalar
  print "$_ \n";
}
close(IN);

