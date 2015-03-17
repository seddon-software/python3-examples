############################################################
#
#	Mouse Events
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Mouse Events");
  $mw->minsize(300, 300);

  $label = $mw->Label(-text => "Press a mouse button");
  $label->pack(-side => "bottom");

  $canvas = $mw->Canvas(-cursor => "dot");
  $canvas->pack(-side   => "left",
                -fill   => "both",
                -expand => 1);

  $canvas->Tk::bind("<Button-1>", [ \&Callback, Ev('b') ]);
  $canvas->Tk::bind("<Button-2>", [ \&Callback, Ev('b') ]);
  $canvas->Tk::bind("<Button-3>", [ \&Callback, Ev('b') ]);

  MainLoop;

sub Callback 
{
  my ($canvas, $button) = @_;
  $label->configure(-text => "Left button pressed")   if($button == 1);
  $label->configure(-text => "Middle button pressed") if($button == 2);
  $label->configure(-text => "Right button pressed")  if($button == 3);
}

