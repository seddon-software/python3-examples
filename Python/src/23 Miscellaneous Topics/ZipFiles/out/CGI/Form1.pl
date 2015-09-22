#! C:/Perl/bin/perl.exe
############################################################
#
#                Form1
#
############################################################

# invoke using a URL of the form
#  http://localhost:8080/cgi-bin/Form1.pl

use CGI qw(:standard);

my $Name = param("Name");
my $Age  = param("Age");

print header();
print start_html("Simple Form");
print h1("Personal details ...");

print start_form("get", "Form1.pl");

print hr();
print h3(("Name:"), textfield("Name", $Name));
print h3(("Age: "), textfield("Age",  $Age));
print p(submit("go"));
print reset("abort");
print hr();
print end_form();


print h2("Name= ", $Name, ", Age= ", $Age);
print end_html();
