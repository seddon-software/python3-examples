############################################################
#
#	Button Styles
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Button Styles");
  $mw->minsize(300, 300);

  $b1 = $mw->Button(-text => "flat button")  ->pack(-pady => 10);
  $b2 = $mw->Button(-text => "groove button")->pack(-pady => 100);
  $b3 = $mw->Button(-text => "raised button")->pack(-pady => 10);
  $b4 = $mw->Button(-text => "ridge button") ->pack(-pady => 10);
  $b5 = $mw->Button(-text => "sunken button")->pack(-pady => 10);
  $b6 = $mw->Button(-text => "solid button") ->pack(-pady => 10);

  $b1->configure(-relief => "flat",   -background => "#ff0000");
  $b2->configure(-relief => "groove", -background => "#df2020");
  $b3->configure(-relief => "raised", -background => "#bf4040");
  $b4->configure(-relief => "ridge",  -background => "#9f6060");
  $b5->configure(-relief => "sunken", -background => "#7f8080");
  $b6->configure(-relief => "solid",  -background => "#5fa0a0");

  MainLoop;
