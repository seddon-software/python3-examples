##################################################
#
#   Advanced pattern matching ...
#
##################################################

$string = "AAAA1111BBBB2222CCCC3333DDDD";

# using greedy matching
$pattern = "^(.+)(\\d+)(.+)\$";
print "$pattern\n";
$string =~ /$pattern/;
print "Greedy:     <$1><$2><$3>\n";

# using non-greedy matching
$pattern = "^(.+?)(\\d+)(.+)\$";
print "$pattern\n";
$string =~ /$pattern/;
print "Non-Greedy: <$1><$2><$3>\n";

1;
