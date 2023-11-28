import unittest
from calc import *

class TestCalculationMethod(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2, add(1,1))
        self.assertEqual(-2, add(-3,1))

    def test_multiply(self):
        self.assertEqual(4, multiply(2,2))
    
    def test_power(self):
        self.assertEqual(16, power(2,4))
    

    
    
if __name__ == '__main__':
    unittest.main()