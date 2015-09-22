#######################################################
#
#       Pipes
#
#######################################################

use strict;
use warnings;

my $IN_PIPE;

my $status;
$status = system("dir");
#$status = qx/dir/;

open($IN_PIPE, "dir/b | ") or die "can't open pipe";

my $line; 
$line = <$IN_PIPE>;
$line = <$IN_PIPE>;
$line = <$IN_PIPE>;
$line = <$IN_PIPE>;

1