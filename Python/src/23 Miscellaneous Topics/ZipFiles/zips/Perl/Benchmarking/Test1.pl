
sub f1 {
    return (10 .. 1000);
}

sub f2 {
    return (10 .. 10000);
}

sub f3 {
    return (10 .. 100000);
}

sub compare {
	print "Comparing functions ... \n";

    use Benchmark qw(cmpthese);
    cmpthese 
        -10, 
        {
            f1 => 'f1()',
            f2 => 'f2()',
            f3 => 'f3()',
        }
}

compare();

1;
