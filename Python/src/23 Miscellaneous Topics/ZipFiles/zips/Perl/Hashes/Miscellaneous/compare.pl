my %h1 = ('A' => 10, 
          'B' => 20,
          'C' => 30,
          'D' => 40);

my %h2 = ('A' => 10, 
          'B' => 21,
          'C' => 30,
          'E' => 40);

my %h3 = (%h1, %h2);
my @keys = keys %h3;

my %h4;

for $key (@keys)
{
	$h4{$key} = $h1{$key} - $h2{$key};
	1; 
}




1;
          