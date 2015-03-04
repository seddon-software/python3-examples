##########################################################
#
#	hash of hashes
#
##########################################################


# create two hashes

$salary{"steve"}  = "25000";
$salary{"mary"}   = "31000";
$salary{"bill"}   = "19870";
$salary{"kalif"}  = "23500";
$salary{"ash"}    = "52000";

$departments{"sales"}       = "DEPT_456";
$departments{"marketing"}   = "DEPT_303";
$departments{"engineering"} = "DEPT_119";
$departments{"hr"}          = "DEPT_295";

# create master hash

$master{"salary"}      = \%salary;
$master{"departments"} = \%departments;

# perform alookup

print "Enter hash: ";
chomp($hash = <STDIN>);

print "Enter key: ";
chomp($key = <STDIN>);

$theHashRef = $master{$hash};
print "Value is: ", $$theHashRef{$key};


