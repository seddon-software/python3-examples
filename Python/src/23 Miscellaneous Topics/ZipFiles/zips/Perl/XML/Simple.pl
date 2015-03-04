##########################################################
#
#             Using the Parser
#
##########################################################



use XML::Parser;
$parser = new XML::Parser('Style' => 'Debug');
$parser->parsefile("book.xml");
1;


