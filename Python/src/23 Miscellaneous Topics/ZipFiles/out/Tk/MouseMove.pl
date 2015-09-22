############################################################
#
#	Mouse Move
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Mouse Move");
  $mw->minsize(500, 500);

  $canvas = $mw->Canvas(-cursor => "pencil");

  $canvas->pack(-side   => "left",
                -fill   => "both",
                -expand => 1);

  $canvas->Tk::bind("<Motion>", [ \&Callback, Ev("x"), Ev("y") ]);

  MainLoop;

sub Callback 
{
  my ($canvas, $x, $y) = @_;
  $canvas->createOval($x, $y, $x + 20, $y + 20, -outline => "red");
}

