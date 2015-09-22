##########################################################
#
#        Test Person Module
#
##########################################################

use strict;
use lib '.';

use Person;

my $charles = new Person("Charles", 48);
my $silvia = new Person("Silvia", 23);

$charles->display();
$silvia->display();

$charles->oneYearOlder();
$silvia->oneYearOlder();

$charles->display();
$silvia->display();


1
