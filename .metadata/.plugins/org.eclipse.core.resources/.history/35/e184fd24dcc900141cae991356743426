##########################################################
#
#   SAX Handlers
#
##########################################################



use XML::Parser;

my $flag = 0;
my $cost = 0.0;
$p1 = new XML::Parser();
$p1->setHandlers( Start   => \&handle_start,
                  End     => \&handle_end,
                  Element => \&handle_element,
                  Char    => \&handle_text );
$p1->parsefile("book.xml");
print "cost = $cost \n";


#######################################################

sub handle_start()
{
  my ($parser, $element, @attributes) = @_;
  print $parser->current_line, ": < $element >\n";
  my %attributes = @attributes;

  foreach $attribute ( keys %attributes ) {
    print "$attribute: $attributes{$attribute}\n";
  }
  if($element == 'cost') {
  	$flag = 1;
  } else {
  	$flag = 0;
  }
}

sub handle_end
{
  my ($parser, $element) = @_;
  print "element end: $element \n";
}

sub handle_element
{
	print "Element def: \n";
}

sub handle_text
{
  my ($parser, $text) = @_;
  print "text: $text \n";
  
  if($flag) {
  	$cost = $text;
  	$flag = 0;
  }
}

