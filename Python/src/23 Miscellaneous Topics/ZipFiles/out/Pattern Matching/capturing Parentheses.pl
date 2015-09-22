##################################################
#
#   Advanced pattern matching ...
#
##################################################


my $string = "AAAA1111BBBB2222CCCC";

# using the x modifier
$string =~ m{^(             # $1
                (           # $2
                  (\D+)     # $3
                  (\d+)     # $4
                )
                (           # $5
                  (\D+)     # $6
                  (\d+)     # $7
                )
                  (\D+)     # $8
              )$}x;

print "\$1:<$1>\n";
print "\$2:<$2>\n";
print "\$3:<$3>\n";
print "\$4:<$4>\n";
print "\$5:<$5>\n";
print "\$6:<$6>\n";
print "\$7:<$7>\n";
print "\$8:<$8>\n";


1;
