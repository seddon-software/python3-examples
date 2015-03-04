##################################################
#
#   Advanced pattern matching ...
#
##################################################

# using the g modifier (remember previous position)
$text = "AB12CD34EF56GH";


while($text =~ /(\d+)/g) {
  print "<$1>\n";
  1;
}

# using the G anchor (represents previous position)
$text =~ /(\d+)/g;      print pos($text), " <$1>\n";
$text =~ /(\d+)/g; print pos($text), " <$1>\n";
$text =~ /\G.*?(\d+)/g; print pos($text), " <$1>\n";


1;
