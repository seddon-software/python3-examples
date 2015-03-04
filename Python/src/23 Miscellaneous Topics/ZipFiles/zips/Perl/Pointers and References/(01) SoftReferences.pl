our $count = 100;

# create a soft reference (to a global)
my $varName = "count";

print "$count \n";
print "$$varName \n";

# increment global
$count++;
print "$count \n";
print "$$varName \n";

# increment through the soft reference
$$varName++;
print "$count \n";
print "$$varName \n";


1
