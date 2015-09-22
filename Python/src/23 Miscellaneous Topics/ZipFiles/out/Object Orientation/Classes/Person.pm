##########################################################
#
#        Person Module
#
##########################################################

package Person;

sub new {
  my ($class, $name, $age) = @_;
  my %attributes = ( 'name'  => $name,
                     'age'   => $age );
  bless  \%attributes, $class;
  return \%attributes;
}

sub display {
  my ($self) = @_;
  print "Name = $self->{'name'} \n";
  print "Age  = $self->{'age'} \n";
}

sub oneYearOlder {
  my ($self) = @_;
  $self->{'age'}++;
}

1;
