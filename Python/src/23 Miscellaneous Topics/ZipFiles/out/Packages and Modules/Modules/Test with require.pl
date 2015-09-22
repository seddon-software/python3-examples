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

# require: loads module into memory at run time
require "ModuleA.pm";

ModuleA::f1();
ModuleA::f2();
ModuleA::f3();

# require: loads module into memory at run time
#          errors will be picked up now
#          this will be AFTER calls to ModuleA
require "ModuleB.pm";

ModuleB::f1();
ModuleB::f2();
ModuleB::f3();
ModuleB::g1();
ModuleB::g2();
ModuleB::g3();
