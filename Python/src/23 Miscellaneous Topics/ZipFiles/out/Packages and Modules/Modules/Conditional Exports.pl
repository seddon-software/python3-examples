##########################################################
#
#	Conditional Exports
#
##########################################################


use lib './mylib';
use ModuleA 'f1','f2';	# make these functions appear local

# fully qualified names always work for exported functions
ModuleA::f1();
ModuleA::f2();
ModuleA::f3();

# now try local names (only f1 and f2 can be used)
f1();
f2();
#f3();		# not exported as local
1

