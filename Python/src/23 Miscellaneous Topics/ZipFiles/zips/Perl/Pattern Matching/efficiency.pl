use Time::HiRes qw(gettimeofday); 

$L_ = qw{[a-z]+};
$N_ = qw{[0-9]+};
$SPACES_ = qw{\s+};

my $part0 = "$L_$SPACES_$L_$SPACES_$L_";
my $part1 = "$L_$SPACES_$L_$SPACES_$N_";
my $part2 = "$L_$SPACES_$N_$SPACES_$L_";
my $part3 = "$L_$SPACES_$N_$SPACES_$N_";
my $part4 = "$N_$SPACES_$L_$SPACES_$L_";
my $part5 = "$N_$SPACES_$L_$SPACES_$N_";
my $part6 = "$N_$SPACES_$N_$SPACES_$L_";
my $part7 = "$N_$SPACES_$N_$SPACES_$N_";


$data = "254  hello  world  547";

my $pattern = "($part0|$part1|$part2|$part3|$part4|$part5|$part6|$part7)";
DoIt($data, $pattern);

$pattern = "($L_|$N_)$SPACES_($L_|$N_)$SPACES($N_|$L_)";
DoIt($data, $pattern);


#######################################################

sub DoIt
{
	my ($data, $pattern) = @_;
    my $start = TimeIt();
	for $i (1 .. 1000) {
        $data =~ m{$pattern};		
	}
	my $end = TimeIt();
	print "Time taken was ", ($end - $start), " seconds\n";
}

sub TimeIt
{
	my ($seconds, $microseconds) = gettimeofday();
	1;
	return $seconds + $microseconds/1000.0;
	
}

1;