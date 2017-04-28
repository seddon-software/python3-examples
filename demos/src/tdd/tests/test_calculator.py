import unittest, sys
sys.path.append('../src')
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.c = Calculator()
    def test_add3To4ToGet7(self):
        actual = self.c.add(3, 4)
        self.assertEquals(7, actual)
    def test_addTwoIntegers(self):
        actual = self.c.add(5, 8)
        self.assertEquals(13, actual)
    def test_invalidFirstArgThrowsException(self):
        self.assertRaises(ValueError, self.c.add, "three", 6)