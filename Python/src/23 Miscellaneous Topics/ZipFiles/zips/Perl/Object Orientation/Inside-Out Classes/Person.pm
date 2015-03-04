##########################################################
#
#        Person Module
#
##########################################################

use strict;

package Person;
use Class::Std::Utils;      # for ident function

{
	# attributes
	my %name_of;
	my %age_of;

	# methods
	sub new {
		my ( $class, $name, $age ) = @_;

		my $object_ref = bless \do { my $anon_scalar }, $class;
        $name_of{ ident $object_ref } = $name;
        $age_of { ident $object_ref } = $age;

		return $object_ref;
	}

	sub display {
		my ($self) = @_;
        print "Name = ",  $name_of{ ident $self };
        print ", Age = ", $age_of { ident $self };
        print "\n";
		1;
	}
	
	sub oneYearOlder {
		my ($self) = @_;
		$age_of { ident $self }++;
	}

}
return 1;
