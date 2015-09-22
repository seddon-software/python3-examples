#! C:/Perl/bin/perl.exe
############################################################
#
#                Param Macro
#
############################################################

# Invoke browser with a URL of the form
#  http://localhost:8080/cgi-bin/Param Macro.pl?Name=Julius&Age=2100

use CGI qw(param);

print <<HTML;
Content-type: text/html

<HTML>
        <HEAD>
        <TITLE>Goodbye World</TITLE>
        </HEAD>
        <BODY>
        <H1>Missing you already</H1>
HTML

my $Name = param("Name");
my $Age  = param("Age");

print "<H2>Name: $Name</H2>";
print "<H2>Age:  $Age</H2>";
print "</BODY>\n";
print "</HTML>";
