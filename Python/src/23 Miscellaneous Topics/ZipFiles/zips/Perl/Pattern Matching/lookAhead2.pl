#######################################################
#
#       lookahead
#
#######################################################

# Search criteria:
# 1) must have some digits in string
# 2) must be a floating point number

use strict;
use warnings;
my ($pattern, $test, $success, $result, $n, @n, %tests);

%tests = (1 => "23.96; PASS", 
          2 => "  .96; PASS", 
          3 => "23.  ; PASS", 
          4 => "  . 8; FAIL",
          5 => "abcde; FAIL",
          6 => "ab.2e; PASS");
@n = (1 .. 6);

my $try1 = qw{\d+\.\d+};
my $try2 = qw{\d*\.\d*};
my $try3 = qw{(\d+\.\d*)|(\d*\.\d+)};
my $try4 = qw{(?=.*\d)(\d*\.\d*)};

$pattern = $try4;
for $n (@n)
{
	my ($data, $expected) = split(m{;[ ]*}, $tests{$n});
	$success = $data =~ m{$pattern};
	$result = $success ? "PASS" : "FAIL";
	$result = $result eq $expected ? "PASS" : "FAIL";
    print "$n: $data \t $result \n";	
}
1;
