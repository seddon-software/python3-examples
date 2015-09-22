############################################################
#
#	Pack
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Pack");
  $mw->minsize(300, 300);

  $b1 = $mw->Button(-text => "1");
  $b2 = $mw->Button(-text => "2");
  $b3 = $mw->Button(-text => "3");
  $b4 = $mw->Button(-text => "4");
  $b5 = $mw->Button(-text => "5");
  $b6 = $mw->Button(-text => "6");
  $b7 = $mw->Button(-text => "7");
  $b8 = $mw->Button(-text => "8");
  $b9 = $mw->Button(-text => "9");
  $b10 = $mw->Button(-text => "10");
  $b11 = $mw->Button(-text => "11");
  $b12 = $mw->Button(-text => "12");

  @left   = (-side => 'left',   -expand => 1, -fill => 'x');
  @right  = (-side => 'right',  -expand => 1, -fill => 'x');
  @top    = (-side => 'top',    -expand => 1, -fill => 'y');
  @bottom = (-side => 'bottom', -expand => 1, -fill => 'y');

  $b1->pack(@left);
  $b2->pack(@left);
  $b3->pack(@left);

  $b4->pack(@right);
  $b5->pack(@right);
  $b6->pack(@right);

  $b7->pack(@top);
  $b8->pack(@top);
  $b9->pack(@top);

  $b10->pack(@bottom);
  $b11->pack(@bottom);
  $b12->pack(@bottom);

  MainLoop;

