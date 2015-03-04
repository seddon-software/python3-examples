############################################################
#
#	Menus
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Menus");
  $mw->minsize(300, 300);

  my $frame = $mw->Frame(-relief      => "ridge",
                         -borderwidth => 2);
  $frame->pack(-side   => "top",
               -anchor => "n",
               -expand => 1,
               -fill   => "x");
  $label = $mw->Label(-text => "Select a menu option")->pack;

  $menuButton1 = $frame->Menubutton(-text => "File",   -tearoff => 0);
  $menuButton2 = $frame->Menubutton(-text => "Edit",   -tearoff => 1);
  $menuButton3 = $frame->Menubutton(-text => "Format", -tearoff => 0);
  $menuButton4 = $frame->Menubutton(-text => "Help",   -tearoff => 0);

  $menuButton1->pack(-side => "left");
  $menuButton2->pack(-side => "left");
  $menuButton3->pack(-side => "left");
  $menuButton4->pack(-side => "right");

  $menuButton1->AddItems(["command" => "New",        -command => \&goNew]);
  $menuButton1->AddItems(["command" => "Open...",    -command => \&goOpen]);
  $menuButton1->AddItems(["command" => "Save",       -command => \&goSave]);
  $menuButton1->AddItems(["command" => "Save As...", -command => \&goSaveAs]);

  $menuButton2->AddItems(["command" => "Cut",        -command => \&goCut]);
  $menuButton2->AddItems(["command" => "Copy",       -command => \&goCopy]);
  $menuButton2->AddItems(["command" => "Paste",      -command => \&goPaste]);

  $menuButton3->AddItems(["command" => "Word Wrap",  -command => \&goWordWrap]);
  $menuButton3->AddItems(["command" => "Font",       -command => \&goFont]);

  $menuButton4->AddItems(["command" => "About",      -command => \&goAbout]);

  MainLoop;

sub goNew      { $label->configure(-text => "New      \n"); }
sub goOpen     { $label->configure(-text => "Open     \n"); }
sub goSave     { $label->configure(-text => "Save     \n"); }
sub goSaveAs   { $label->configure(-text => "SaveAs   \n"); }
sub goCut      { $label->configure(-text => "Cut      \n"); }
sub goCopy     { $label->configure(-text => "Copy     \n"); }
sub goPaste    { $label->configure(-text => "Paste    \n"); }
sub goWordWrap { $label->configure(-text => "WordWrap \n"); }
sub goFont     { $label->configure(-text => "Font     \n"); }
sub goAbout    { $label->configure(-text => "About    \n"); }

