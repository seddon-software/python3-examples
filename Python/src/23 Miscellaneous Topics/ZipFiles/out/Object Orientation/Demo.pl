
my $p1 = new Point(100, 200);
my $p2 = new Point( 50, 500);
my $p3 = new Point(250, 170);

$p1->MoveBy(10, 20);
$p2->MoveBy(10, 20);
$p3->MoveBy(10, 20);

$p1->WhereAreYou();
$p2->WhereAreYou();
$p3->WhereAreYou();

1;


package Point;

sub new
{
	print "@_ \n";
	my ($class, $x, $y) = @_;
	
	my $ref = {'x' => $x, 'y' => $y};
    bless $ref, $class; 	
	return $ref;
}

sub MoveBy
{
	my ($self, $dx, $dy) = @_;
	
    $self->{'x'} += $dx;
    $self->{'y'} += $dy;
	
}

sub WhereAreYou
{
    my ($self) = @_;
    
    print "Point is at: $self->{'x'}, $self->{'y'} \n";
}
