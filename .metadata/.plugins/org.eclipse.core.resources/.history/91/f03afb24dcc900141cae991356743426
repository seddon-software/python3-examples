############################################################
#
#	Named Parameters
#
############################################################


sub volume {
    my %params = @_;    # pack into a hash

    my ($height, $width, $length) =
                         @params{'-height', '-width', '-length'};
    print "Height = $height \n";
    print "Width  = $width  \n";
    print "Length = $length \n";

    my $volume = $height * $width * $length;
    print "Volume = $volume \n";
    print "-------------\n";
}

# use named parameters in any order
volume('-height' => 10, '-width'  => 20, '-length' => 30);
volume('-width'  => 20, '-height' => 10, '-length' => 30);
volume('-length' => 30, '-height' => 10, '-width'  => 20);
1;