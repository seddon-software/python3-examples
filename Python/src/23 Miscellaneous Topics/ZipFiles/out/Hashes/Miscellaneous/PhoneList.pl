##########################################################
#
#	hashes
#
##########################################################


#            Key(Name) => Values(Phone)


%PhoneBook = ("John"   => "7145",
	      	  "Mary"   => "3110",
	          "Steven" => "4669",
	          "Angela" => "2201",
	          "Bjorn"  => "5989");
PrintEntry("Angela");
PrintKeys();
PrintValues();
PrintBoth();


############################################################

sub PrintEntry
{
	my ($name) = @_;
	$phone = $PhoneBook{$name};
	print "Name = $name, Phone = $phone \n";
}

sub PrintKeys()
{
	foreach $name (keys(%PhoneBook))
	{
	  print "$name \n";
	}
}

sub PrintValues()
{
	foreach $phone (values(%PhoneBook))
	{
	  print "$phone \n";
	}
}

sub PrintBoth()
{
	while (($name, $phone) = each(%PhoneBook))
	{
	  print "Name = $name, Phone = $phone \n";
	}
}
