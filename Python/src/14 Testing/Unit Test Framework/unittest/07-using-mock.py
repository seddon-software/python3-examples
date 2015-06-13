# Mock is designed for use with unittest. 
# Mock is based on the 'action -> assertion' pattern instead 
# of 'record -> replay' used by many mocking frameworks.

from mock import patch, Mock
import unittest


class MyClass():
    'This method is mocked out'
    def my_method(self):
        # this method will do something complicated in practice
        # and we don't wan't it to take part in the test
        pass
 
class AnotherClass():
    'We are testing this method'
    def f(self):
        myclass = MyClass()
        return myclass.my_method()
    

class testPoint(unittest.TestCase):
    'testing a method mocked out with a constant return value (True)'
    @patch.object(MyClass, 'my_method')
    def test_mocking_a_method(self, mocked_method):
        mocked_method.return_value=True
        o =  AnotherClass()
        result = o.f()
        self.assertTrue(result)

    'testing a method mocked out which returns the successive results (False, False, True)'
    @patch.object(MyClass, 'my_method')
    def test__mocking_a_method_with_multiple_return_values(self, mocked_method):
        return_values= [False,False,True]
        def side_effect():
            return return_values.pop()
        mocked_method.side_effect = side_effect

        o =  AnotherClass()
        self.assertTrue(o.f())
        self.assertFalse(o.f())
        self.assertFalse(o.f())

if __name__ == '__main__':
    unittest.main()
    1
