##########################################################
#
#        Capture Variables
#
##########################################################

my $string = "1111222233333333333344445555555566667777";
my $pattern = "2+(3+)4+(5+)6+";

# match pattern
$string =~ /$pattern/;

# print results
print "\$` is <$`> \n";
print "\$& is <$&> \n";
print "\$' is <$'> \n";
print "\$1 is <$1> \n";
print "\$2 is <$2> \n";


1