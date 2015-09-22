##########################################################
#
#	Default File Handle 
#
##########################################################


print '@ARGV: ';
print "@ARGV \n";

print "Using ARGV as file handle\n";

while(<>)
{
  print '$ARGV:' . "$ARGV: ";
  print;
}

1