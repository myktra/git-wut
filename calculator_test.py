"""A test for the add function"""

import unittest

from calculator import add

class CalculatorTest(unittest.TestCase):
    """A test for the calculator"""
    def test_add(self):
        """Test that the add function returns the correct result"""
        self.assertEqual(add(1, 2), 4)

if __name__ == '__main__':
    unittest.main()