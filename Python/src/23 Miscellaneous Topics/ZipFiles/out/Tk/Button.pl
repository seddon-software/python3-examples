############################################################
#
#	Button
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Button");
  $mw->minsize(300, 300);

  $button = $mw->Button(-text => "Button", 
                        -activebackground => "red");
  $button->pack;

  MainLoop;

