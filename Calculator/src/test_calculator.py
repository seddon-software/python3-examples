from Calculator import *
import unittest


class TestCalculatorClass(unittest.TestCase):
    """
    A test class for the Calculator class
    """
    def setUp(self):
        self.c = Calculator()

    def testWeCanAddTwoNumbers(self):
        r = self.c.add(5, 6)
        self.assertEqual(11, r)
        
    def testExceptionIfWeAddTwoStrings(self):
        self.assertRaises(TypeError, lambda _: self.c.add("5", "6"))

    def testExceptionIdWeAddTwoStrings2(self):
        self.assertRaises(TypeError, self.c.add, "5", "6")


if __name__ == '__main__':
    unittest.main()
    1
    