use XML::LibXML;


# create a parser
my $parser = XML::LibXML->new;

# open input document and parse to create DOM tree
open(my $fh, "<", "book.xml") || die "can't open book.xml";
binmode $fh;    # drop all PerlIO layers possibly created by a use open pragma
my $doc = $parser->parse_fh($fh);

# create a new XML fragment
my $element = XML::LibXML::Element->new("copies");
$element->setAttribute("number", 8);
$element->appendText("several copies");

# append fragment to root node
my $root = $doc->documentElement();
@pubdates = $doc->findnodes("//pubdate");
$pubdate = $pubdates[0];

#$root->appendChild($element);
$pubdate->appendChild($element);

# copy DOM tree to output file
open(my $out, ">", "out.xml") || die "can't open out.xml";
binmode $out;    # as above
print $out $doc->toString();
print $doc->toString(); # echo to screen


1