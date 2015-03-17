package point;

sub new {
	my ($classname, $x0, $y0) = @_;
	my %attributes = ( 'x' => $x0, 'y' => $y0);
	bless \%attributes, $classname;
	return \%attributes;
	1;
}

sub moveBy {
	my ($self, $dx, $dy) = @_;
	$self->{'x'} += $dx;
	$self->{'y'} += $dy;
}

1
