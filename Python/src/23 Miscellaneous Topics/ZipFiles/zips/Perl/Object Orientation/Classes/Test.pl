##########################################################
#
#        Test Person Module
#
##########################################################

use lib '.';
use Person;

$charles = new Person("Charles", 48);
$silvia = new Person("Silvia", 23);

$charles->display();
$silvia->display();

$charles->oneYearOlder();
$silvia->oneYearOlder();

$charles->display();
$silvia->display();


1