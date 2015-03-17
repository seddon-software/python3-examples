#! C:/Perl/bin/perl.exe
############################################################
#
#                Form2.pl
#
############################################################

# invoke using a URL of the form
# http://localhost:8080/cgi-bin/Form2.pl

use CGI;

$page = new CGI;

print $page->header();
print $page->start_html(-title => "Form 2");
print $page->h1("Form 2");
print $page->hr();
GeneratePage();
print $page->end_html();


sub GeneratePage()
{
  if($page->param) {
    print $page->p("Parameters present");
    UpdateForm();
  } else {
    print $page->p("No parameters found");
    CreateForm();
  }
}

sub CreateForm()
{
  print $page->start_form(-method => "get");
  print $page->p();
  print $page->popup_menu(-name => 'NAME',
                          -value => [qw/red green blue/],
                          -default => 'blue');
  print $page->hr();
  print $page->submit("Submit");
  print $page->p();
  print $page->reset("Reset");
  print $page->end_form();
}

sub UpdateForm()
{
  $name = $page->param('NAME');
  print $page->p("Selected option: $name");
}
