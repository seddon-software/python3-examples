##########################################################
#
#        Rectangle
#
##########################################################

package Rectangle;
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
    print "Draw Rectangle \n";
}

return 1;
