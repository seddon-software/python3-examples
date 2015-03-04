##########################################################
#
#	Split
#
##########################################################

my @words;
@words = split('\s',  "The quick    brown fox jumps over the lazy dog.");
@words = split('\s+', "The quick    brown fox jumps over the lazy dog.");
my $x = split(' ', "The quick brown   fox jumps over the lazy dog.");

print "3rd word is: $words[2] \n";
print "size is: $x \n";
