############################################################
#
#	Disabling Buttons
#
############################################################

# demonstrate changing a button's colour when active and
# toggling the button between enabled and disabled


  use Tk;

  my $mw = new MainWindow;
  $mw->title("Disable");
  $mw->minsize(300, 300);


  $buttonExit = $mw->Button(-text => "Exit",
                            -activebackground => "red", 
                            -command => sub { exit });

  $title = "Disable Exit";
  $buttonToggle = $mw->Button(-textvariable => \$title, 
                              -command => \&callback);

  $buttonToggle->pack;
  $buttonExit->pack;

  MainLoop;


sub callback
{
  # toggle the state of the exit button
  if($buttonExit->cget(-state) eq "disabled") {
    $title = "Disable Exit";
    $buttonExit->configure(-state => "normal");
  } else {
    $title = "Enable Exit";
    $buttonExit->configure(-state => "disabled");
  }
}
