use Readonly;

Readonly my $var   => 100;
Readonly my @array => ( 20 .. 25 );
Readonly my %hash  => ( 'a' => 65, 'b' => 66 );

# attempt to modify constant scalar
eval { 
	$var++; 
};
print "Error: $@ \n" if ($@);


# attempt to modify constant array
eval { 
	$array[0]++; 
};
print "Error: $@ \n" if ($@);


# attempt to modify constant hash
eval { 
	$hash{'a'}++; 
};
print "Error: $@ \n" if ($@);

1;

