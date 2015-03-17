##########################################################
#
#        polymorphism
#
##########################################################

use lib '.';

use Rectangle;
use Trapezoid;
use Ellipse;

# create polymorphic collection of shapes
@list = (new Ellipse,
         new Rectangle,
         new Trapezoid,
         new Rectangle,
         new Ellipse,
         new Rectangle);

# ask each shape to draw itself (polymorphic binding)
foreach $ptr (@list) {
    $ptr->Draw();
}







