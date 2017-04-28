import unittest, sys
sys.path.append('../src')
from calculator import Calculator
 
class TddInPythonExample(unittest.TestCase):
 
    def setUp(self):
       self.calc = Calculator()

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2,2)
        self.assertEqual(4, result)

    def test_calculator_add_method_returns_correct_result2(self):
        result = self.calc.add(2,7)
        self.assertEqual(9, result)
            
    def test_3(self):
        call = self.calc.add, 'two', 'three'
        self.assertRaises(ValueError, *call)
            
    def test_4(self):
        self.assertRaises(ValueError, self.calc.add, 6, 'three')

    def test_5(self):
        self.assertRaises(ValueError, self.calc.add, 'three', 6)
        