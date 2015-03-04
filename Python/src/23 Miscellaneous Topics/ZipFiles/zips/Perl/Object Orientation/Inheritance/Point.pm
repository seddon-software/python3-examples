##########################################################
#
#        Point
#
##########################################################

package Point;

sub new {
    my ($class, $x0, $y0) = @_;
    print "$_[0] \n";

    my %data = ( 'x' => $x0,
                 'y' => $y0 );
    bless  \%data, $class;
    return \%data;
}

sub MoveBy {
    my ($objRef, $x, $y) = @_;
    $objRef->{'x'} += $x;
    $objRef->{'y'} += $y;
}

sub GetDetails {
    my ($objRef) = @_;

    my $x = $objRef->{'x'};
    my $y = $objRef->{'y'};
    return "$x, $y";
}

sub Display {
    my ($objRef) = @_;
    print "Point: " . $objRef->GetDetails() . "\n";
}

return 1;
