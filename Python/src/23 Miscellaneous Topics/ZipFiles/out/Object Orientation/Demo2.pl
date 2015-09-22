package Point;

sub new
{
	my ($self, $x, $y) = @_;
	my $ref = {'x' => $x, 'y' => $y};
	bless $ref, "Point";
	return $ref;
}

sub MoveBy
{
	my ($self, $dx, $dy) = @_;
    $self->{'x'} += $dx;
    $self->{'y'} += $dy;
}

package Main;

print "Hello";

my $p = new Point(3,6);
$p->MoveBy(1,1); 
1
