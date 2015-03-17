############################################################
#
#	Counter
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Counter");
  $mw->minsize(300, 300);

  $label = $mw->Label(-text => "0",
                      -font => "Arial 40")->pack;
  $label->repeat(1000, \&EverySecond);

  MainLoop;


sub EverySecond {
  $count++;
  $label->configure(-text => $count);
}