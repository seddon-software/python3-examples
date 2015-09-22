############################################################
#
#	Default Parameters
#
############################################################


sub volume {
    my %params = ('-height' => 10, # set up defaults
                  '-width'  => 10,
                  '-length' => 10,
                   @_);    # overwrite with passed parameters

    my ($height, $width, $length) =
                         @params{'-height', '-width', '-length'};
    print "Height = $height \n";
    print "Width  = $width  \n";
    print "Length = $length \n";

    my $volume = $height * $width * $length;
    print "Volume = $volume \n";
    print "-------------\n";
}

# use named parameters in any order, possibly using defaults
volume('-height' => 10, '-width'  => 20, '-length' => 30);
volume('-width'  => 20, '-length' => 30);
volume('-length' => 30);
volume();

1;