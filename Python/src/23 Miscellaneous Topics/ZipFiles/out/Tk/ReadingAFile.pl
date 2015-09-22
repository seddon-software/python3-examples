############################################################
#
#	Reading A File
#
############################################################

  use Tk;

  my $mw = new MainWindow;
  $mw->title("Reading A File");
  $mw->maxsize(300, 300);

  $text = $mw->Scrolled("Text")->pack;
  $text->configure(-background => "yellow",
                   -foreground => "blue",
                   -height     => 10,
                   -font       => "Arial 20",
                   -wrap       => "none");

  open(MYFILE, "myfile.txt") || die "could not open test file";

  while(<MYFILE>) {
    $text->insert('end', $_);
  }

  close(MYFILE);

  MainLoop;

