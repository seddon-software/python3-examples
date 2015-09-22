##################################################
#
#     Passing File Handles to Subroutines
#
##################################################

sub PrintFile
{
	my ($FH) = @_;
    @lines = <$FH>;
    print "@lines";	
}

use IO::Handle;

#
# method 1 - use a typeglob (doesn't work with strict)
#
open(IN, "./test.txt") || die "can't open file \n";
PrintFile(*IN);

#
# method 2 - use a IO::Handle (works with strict)
#
my $fh = IO::Handle->new();
open($fh, "./test.txt") || die "can't open file \n";
PrintFile($fh);



 

1