############################################################
#
#	Checkbuttons
#
############################################################

# set up 3 checkbuttons and display their status in a
# button widget (its display name);
  use Tk;

  my $mw = new MainWindow;
  $mw->title("Checkbuttons");
  $mw->minsize(300, 300);

  # initial settings of checkbuttons
  $value1 = 0;
  $value2 = 1;
  $value3 = 0;

  $mw->Checkbutton(-text     => "Checkbutton 1",
                   -variable => \$value1,
                   -command  => \&callback)->pack;

  $mw->Checkbutton(-text     => "Checkbutton 2",
                   -variable => \$value2,
                   -command  => \&callback)->pack;

  $mw->Checkbutton(-text     => "Checkbutton 3",
                   -variable => \$value3,
                   -command  => \&callback)->pack;

  $statusButton = $mw->Button();
  $statusButton->pack;

  callback();
  MainLoop;

# all 3 checkbuttons use the same callback method

sub callback
{
  $message = $value1 . $value2 . $value3;
  $statusButton->configure(-text => $message);
}