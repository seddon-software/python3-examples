############################################################
#
#	Draw Lines
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Draw Lines");
  $mw->minsize(500, 500);


  $canvas = $mw->Canvas(-cursor => "crosshair");
  $canvas->pack(-side   => "left",
                -fill   => "both",
                -expand => 1);

  @coords = (100, 100, 
             400, 400, 
             200, 400,
             150, 350, 
             100, 100);
  $polygon = $canvas->createLine(@coords, -width => 10);

  MainLoop;




