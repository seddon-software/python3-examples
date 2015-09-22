##########################################################
#
#        hashes and functions
#
##########################################################


# create hash

my %salary;
$salary{"steve"}  = "25000";
$salary{"mary"}   = "31000";
$salary{"bill"}   = "19870";
$salary{"kalif"}  = "23500";
$salary{"ash"}    = "52000";

# pass to function
PrintHash(%salary);



sub PrintHash
{
  my (%theHash) = @_;

  while (($name, $salary) = each(%theHash))
  {
      print "$name \t $salary \n";
  }
}