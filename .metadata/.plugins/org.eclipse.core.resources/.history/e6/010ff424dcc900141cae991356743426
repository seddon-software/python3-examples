##########################################################
#
#        Test Modules
#
##########################################################

# update the include path
sub BEGIN
{
  unshift (@INC, "./mylib");
  print "@INC \n";
}

# use: loads module at compile time
use ModuleA;

ModuleA::f1();
ModuleA::f2();
ModuleA::f3();

# use: loads module at compile time
#      any errors will be spotted early
use ModuleB;
ModuleB::f1();
ModuleB::f2();
ModuleB::f3();
ModuleB::g1();
ModuleB::g2();
ModuleB::g3();
