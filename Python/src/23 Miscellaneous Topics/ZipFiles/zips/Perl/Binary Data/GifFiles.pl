##########################################################
#
#        GIF files
#
##########################################################

CheckIfGIF("Rabbit.gif");
CheckIfGIF("Hare.gif");


sub CheckIfGIF {
    my ($fileName) = @_;

    open(FH, $fileName) or die "Can't open GIF file";
    read(FH, $header, 10);
    ($gifword,$giflevel,$xlo,$xhi,$ylo,$yhi) = unpack("a3a3C4",$header);

    if ($gifword ne "GIF") {
        print ("$fileName is NOT a valid GIF file \n");
    }
    else {
        print ("$fileName is a GIF file - version $giflevel\n");
        $width  = $xhi * 256 + $xlo;
        $height = $yhi * 256 + $ylo;
        print "$width pixels wide by $height pixels high\n";
    }
    print "-------------------------------------- \n";
}
