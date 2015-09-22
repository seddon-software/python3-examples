##########################################################
#
#	split
#
##########################################################



$text = "This line  has\n lots \t  of   white\t  space\n";
@fields = split(/\s+/, $text);

print "$text \n";

foreach $field (@fields)
{
  print "...$field... \n";
}

1