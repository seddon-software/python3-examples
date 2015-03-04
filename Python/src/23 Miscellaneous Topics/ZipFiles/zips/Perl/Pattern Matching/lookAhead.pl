#######################################################
#
#       lookahead
#
#######################################################

use strict;
use warnings;

my $text;

# Positive lookahead
# capture .* followed by Monday or Tuesday (greedy matching)
$text = "Today is Monday but tomorrow will be Tuesday and so on";
$text =~ m{^(.*)(?=Monday|Tuesday)};
print "$1 \n";

# Negative lookahead
# capture .* that is followed by [A-Z], but NOT if next character is u
# so Tuesday will fail
$text = "Today is Monday but tomorrow will be Tuesday and so on";
$text =~ m{^(.*[A-Z])(?!u)};
print "$1 \n";

1;
