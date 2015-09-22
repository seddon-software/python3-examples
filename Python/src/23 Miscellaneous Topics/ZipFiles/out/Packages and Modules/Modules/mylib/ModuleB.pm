##########################################################
#
#        ModuleB
#
##########################################################

package ModuleB;

use Exporter;
@ISA = qw(Exporter);
@EXPORT = qw(f1 f2 f3 g1 g2 g3);

#?                # deliberate error

sub f1 { print "And this is f1 in ModuleB\n"; }
sub f2 { print "And this is f2 in ModuleB\n"; }
sub f3 { print "And this is f3 in ModuleB\n"; }
sub g1 { print "And this is g1 in ModuleB\n"; }
sub g2 { print "And this is g2 in ModuleB\n"; }
sub g3 { print "And this is g3 in ModuleB\n"; }


return 1;
