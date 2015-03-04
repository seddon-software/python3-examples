############################################################
#
#				Frames
#
############################################################


use Tk;

my $mw = new MainWindow;
$mw->title("Frames");
$mw->minsize(300, 300);

CreateFrame(-window => $mw,
            -side   => 'left',
            -colour => 'red',
            -text   => 'L');

CreateFrame(-window => $mw,
            -side   => 'right',
            -colour => 'blue',
            -text   => 'R');

CreateFrame(-window => $mw,
            -side   => 'top',
            -colour => 'yellow',
            -text   => 'T');

CreateFrame(-window => $mw,
            -side   => 'bottom',
            -colour => 'green',
            -text   => 'B');

MainLoop;

sub CreateFrame {
  my %params = @_;
  my ($window, $text, $side, $colour)
                = @params{'-window', '-text', '-side', '-colour'};
	my $frame = $window->Frame(-background => $colour);
  $frame->pack(-side => $side, -fill => 'y', -expand => 'y');
  my $b1 = $frame->Button(-text => $text . '1')->pack(-side => $side);
  my $b2 = $frame->Button(-text => $text . '2')->pack(-side => $side);
  my $b3 = $frame->Button(-text => $text . '3')->pack(-side => $side);
}
