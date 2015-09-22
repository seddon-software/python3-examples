##########################################################
#
#        Trapezoid
#
##########################################################

package Trapezoid;
use lib '.';

use Shape;
@ISA = ('Shape');      # inherits from Shape

sub new {
    my ($class) = @_;
    my $pBase = new Shape();
    bless  \$pBase, $class;
    return \$pBase;
}

sub Draw {
    print "Draw Trapezoid \n";
}

return 1;
