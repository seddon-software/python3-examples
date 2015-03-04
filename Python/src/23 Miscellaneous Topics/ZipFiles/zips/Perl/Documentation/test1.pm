1;

=head1 NAME

Date::Calendar - Calendar objects for different holiday schemes

=head1 MOTTO

There is more than one way to do it - this is just one of them!

=head1 PREFACE

Basically, Date::Calendar is just a caching proxy class for
Date::Calendar::Year objects, which are embedded in each
Date::Calendar object.

However, and in contrast to Date::Calendar::Year methods, Date::Calendar
methods permit calculations spanning an arbitrary number of years, without
loss of efficiency.

=head1 SYNOPSIS

  use Date::Calendar::Profiles qw( $Profiles );
  use Date::Calendar;


=head1 INTERFACE

Note that whenever a year number, a date, a time or a combined
date and time are expected as input parameters by one of the
methods of this class, you can always pass a Date::Calc[::Object]
date object or an array reference (of an array of appropriate
length) instead!
=head1 DESCRIPTION

=over 2

=item *

The first argument must be the reference of a hash,
which contains a holiday scheme or "profile" to be used
in all calculations involving the new calendar object.

The second argument is optional, and must consist of
the valid name or number of a language as provided by
the Date::Calc(3) module if given.

=item *

This method returns a Date::Calendar::Year object for the given
year and the profile that was associated with the given calendar
object.


=item *

This method returns the list of B<YEAR NUMBERS> of the
Date::Calendar::Year objects contained in the given
calendar object's cache.

=item *

This method returns the list of B<OBJECT REFERENCES> of
the Date::Calendar::Year objects contained in the given
calendar object's cache.


=back

=head1 SEE ALSO

Date::Calendar::Year(3), Date::Calendar::Profiles(3),
Date::Calc::Object(3), Date::Calc(3), Bit::Vector(3).

=head1 KNOWN BUGS

The method "add_delta_workdays()" is known to produce results
which are sometimes off by one working day when a negative



