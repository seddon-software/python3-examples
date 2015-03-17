############################################################
#
#	Draw Ovals
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Draw Ovals");
  $mw->minsize(500, 500);


  $canvas = $mw->Canvas(-cursor => "crosshair");
  $canvas->pack(-side   => "left",
                -fill   => "both",
                -expand => 1);

  $x1 = 100; $y1 = 100;
  $x2 = 400; $y2 = 200;

  @coords = ($x1, $y1, $x2, $y2);
  @options = (-width   => 5, 
              -fill    => "yellow",
              -outline => "blue");

  $oval = $canvas->createOval(@coords, @options);

  MainLoop;




