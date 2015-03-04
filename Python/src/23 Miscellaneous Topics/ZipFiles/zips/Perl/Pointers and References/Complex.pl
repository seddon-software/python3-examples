

$ref = { 'a' => 1,
         'b' => 2,
         'c' => { 'x' => 10, 'y' => 11 },
         'd' => [ 20, 21, 22, 23 ]
       };

%hash = %$ref;

$x = $hash{'a'};     print "$x \n";
$x = $$ref{'a'};     print "$x \n";
$x = $ref->{'a'};    print "$x \n";

$y = $hash{'c'}->{'x'};  print "$y \n";
$y = $$ref{'c'}->{'x'};  print "$y \n";

$z = $hash{'d'}->[2];  print "$z \n";
$z = $$ref{'d'}->[2];  print "$z \n";

1;

