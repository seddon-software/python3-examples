##################################################
#
#   Advanced pattern matching ...
#
##################################################

my $string = "AAAA1111BBBB2222CCCC3333DDDD";

# using the x modifier
$string =~ m{         
             ^        # start of line
             (.*?)    # 0 or more characters
                      # non greedy
             (\d+)    # 1 or more digits
             (.*)     # 0 or more characters
             $        # end of line
           }x;
print "<$1><$2><$3>\n";


1;
