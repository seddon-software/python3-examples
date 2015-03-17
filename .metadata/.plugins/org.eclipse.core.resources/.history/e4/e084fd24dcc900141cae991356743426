############################################################
#
#	Scrolling Widgets
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Scrolling Widgets");
  $mw->maxsize(400, 200);

  $text = $mw->Scrolled("Text", -width => 40, -wrap => "none");
  $text->pack(-expand => 2, -fill => "both");

  foreach (qw/FirstName LastName Address1 Address2 Address3 Address4 
              Email Telephone Department Subject1 Subject2 Subject3 
              Subject4/)
  {
    $label = $text->Label(-text => "$_", -relief => "groove", -width => 20);
    $entry = $text->Entry(-width => 20);
    $text->windowCreate("end", -window => $label);
    $text->windowCreate("end", -window => $entry);
    $text->insert('end', "\n");
  }

  MainLoop;

