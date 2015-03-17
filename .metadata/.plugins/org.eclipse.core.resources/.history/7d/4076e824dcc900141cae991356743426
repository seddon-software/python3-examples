#! C:/Perl/bin/perl.exe
############################################################
#
#        CGI macros
#
############################################################

# invoke script with URL of the form
#  http://localhost:8080/cgi-bin/CGI Macros.pl?Name=Julius&Age=2100

use CGI qw(:standard);

print header();
print start_html("CGI Macros");
print h1("Personal details ...");

my $Name = param("Name");
my $Age  = param("Age");

print h2("Name: $Name");
print h2("Age:  $Age");
print end_html();
