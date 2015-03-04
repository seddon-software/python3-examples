############################################################
#
#	Button Images
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Button Images");
  $mw->minsize(300, 300);


  $image = $mw->Photo(-file => "GIFs/radio.gif");
  $button = $mw->Button(-image => $image, -background => "red")->pack;

  MainLoop;
