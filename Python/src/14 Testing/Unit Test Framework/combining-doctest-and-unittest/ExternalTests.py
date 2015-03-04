#!/usr/bin/python
#
#  Example showing how to use doctest with the tests
#  defined in external files
#

def square(x):
    if x > 10:
        raise ValueError('input too large')
    else:
        return x*x

if __name__ == "__main__":
    import doctest, unittest
    print '**running unittest doctest'
    suite = doctest.DocFileSuite('test1.txt', 'test2.txt')
    unittest.TextTestRunner(verbosity=0).run(suite)
    1
