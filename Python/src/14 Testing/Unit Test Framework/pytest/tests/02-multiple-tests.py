############################################################
#
#    multiple tests
#
############################################################

import maths

class TestSquare:
    def setup_class(self):
        self.m = maths.Maths()
    
    def is_square(self, n, expected):
        self.m.setX(n)
        assert self.m.square() == expected

        
    def test_squares(self):
        # set up 5 tests (the last one fails!)
        inputs  = ( 4,  7,  10,  20, 25)
        outputs = (16, 49, 100, 400, -1)
        
        for i, o in zip(inputs, outputs):
            yield self.is_square, i, o
            
