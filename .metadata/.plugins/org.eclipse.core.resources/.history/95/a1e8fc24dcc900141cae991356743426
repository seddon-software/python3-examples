############################################################
#
#	Grid
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Grid");
  $mw->minsize(300, 300);

  $b1 = $mw->Button(-text => "1");
  $b2 = $mw->Button(-text => "2");
  $b3 = $mw->Button(-text => "3");
  $b4 = $mw->Button(-text => "4");
  $b5 = $mw->Button(-text => "5");
  $b6 = $mw->Button(-text => "6");
  $b7 = $mw->Button(-text => "7");
  $b8 = $mw->Button(-text => "8");

  # form a 2 row by 4 col grid
  # where row 0 sticks to N
  # and row 1 sticks to all for sides
  # when resizing your window

  $b1->grid($b2, $b3, $b4, -sticky => "n");
  $b5->grid($b6, $b7, $b8, -sticky => "nsew");

  # weights of each row and column must be set if you
  # want your widgeyts to resize with the window
 
  $mw->gridRowconfigure(0, -weight => 1);
  $mw->gridRowconfigure(1, -weight => 1);
  $mw->gridColumnconfigure(0, -weight => 1);
  $mw->gridColumnconfigure(1, -weight => 1);
  $mw->gridColumnconfigure(2, -weight => 1);
  $mw->gridColumnconfigure(3, -weight => 1);

  MainLoop;

