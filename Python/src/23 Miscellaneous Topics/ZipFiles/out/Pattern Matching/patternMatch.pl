##################################################
#
#   Advanced pattern matching ...
#
##################################################


print "Code: ";
chomp ($pattern=<STDIN>);
chdir("data-files");
open (IN, "codes.txt") or die "can't open input file";

for (<IN>) {
  chomp;
  print ("\$1=<$1>   \$_=<$_>\n") if (m{$pattern});
}

1;


