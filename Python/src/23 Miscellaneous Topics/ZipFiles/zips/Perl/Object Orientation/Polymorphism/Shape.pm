##########################################################
#
#        Shape
#
##########################################################

package Shape;

sub new {
    my ($class) = @_;
    my %data = ();           # keep it simple - empty hash
    bless  \%data, $class;
    return \%data;
}

sub Draw {
    print "Draw Shape \n";
}

return 1;
