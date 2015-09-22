##########################################################
#
#        Test inheritance
#
##########################################################

use lib '.';

use Point;
use ColouredPoint;

#Point
$p  = new Point(100, 200);
$p->Display();

$p->MoveBy(1, 2);
$p->Display();

# ColouredPoint
$cp = new ColoredPoint(1000, 2000, 0, 25);
$cp->Display();

$cp->MoveBy(10, 20);
$cp->Display();

$cp->ChangeColour(7);
$cp->Display();
