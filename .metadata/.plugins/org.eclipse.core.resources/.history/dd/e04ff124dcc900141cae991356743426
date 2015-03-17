##########################################################
#
#        ColouredPoint
#
##########################################################

package ColoredPoint;
use lib '.';

use Point;
@ISA = ('Point');        # derives from Point

sub new {
    my ($class, $x0, $y0, $c, $r) = @_;
    print "$_[0] \n";

    my $pBase = new Point($x0, $y0);

    # update the hash defined by the base class
    $pBase->{'colour'} = $c;
    $pBase->{'radius'} = $r;

    # bless our V-Table
    bless  $pBase, $class;
    return $pBase;
}

sub GetDetails
{
    my ($objRef) = @_;

    # call base class method of the same name
    my $base = $objRef->Point::GetDetails();
    my $c = $objRef->{'colour'};
    my $r = $objRef->{'radius'};

    return "$base, $c, $r";
}

sub ChangeColour
{
    my ($objRef, $newColour) = @_;
    $objRef->{'colour'} = $newColour;
}

sub Display {
    my ($objRef) = @_;
    print "ColouredPoint: " . $objRef->GetDetails() . "\n";
}

return 1;

