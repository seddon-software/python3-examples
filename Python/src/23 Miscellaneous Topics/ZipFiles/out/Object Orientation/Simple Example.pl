##########################################################
#
#        Object Orientation
#
##########################################################

$p1 = new Point;
$p2 = new Point;
$p3 = new Point;

$p1->Initialise(100, 50);
$p2->Initialise(200, 60);
$p3->Initialise(300, 70);

$p1->WhereAreYou();
$p2->WhereAreYou();
$p3->WhereAreYou();

$p1->MoveBy(1, 1);
$p2->MoveBy(2, 2);
$p3->MoveBy(3, 6);

$p1->WhereAreYou();
$p2->WhereAreYou();
$p3->WhereAreYou();

############################################################

package Point;

sub new
{
    my %data = ( 'x' => 0,
                 'y' => 0 );
    bless  \%data, "Point";
    return \%data;
}

sub Initialise
{
    my ($objRef, $x0, $y0) = @_;
    $objRef->{'x'} = $x0;
    $objRef->{'y'} = $y0;
}

sub WhereAreYou
{
    my ($objRef) = @_;
    print "x = $objRef->{'x'}, y = $objRef->{'y'} \n";
}

sub MoveBy
{
    my ($objRef, $dx, $dy) = @_;
    $objRef->{'x'} += $dx;
    $objRef->{'y'} += $dy;
}






