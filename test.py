import unittest
from string_functions import *

class TestToUpper(unittest.TestCase):
    # Test the to_upper functions
    def test_to_upper(self):
        # Assert with all capital letters string
        # Input: "PYTHON"
        # Output: "PYTHON"
        self.assertEqual(to_upper("PYTHON"), "PYTHON")

        # Assert with all small letters string
        # Input: "python"
        # Output: "PYTHON"
        self.assertEqual(to_upper("python"), "PYTHON")

        # Assert with all jumbled letters
        # Input: "pYtHoN"
        # Output: "PYTHON"
        self.assertEqual(to_upper("pYtHoN"), "PYTHON")

        # Assert with empty string
        # Input: ""
        # Output: ""
        self.assertEqual(to_upper(""), "")

        # Assert with a string integer
        # Input: "123"
        # Output: "123"
        self.assertEqual(to_upper("123"), "123")

        # Assert with an integer
        # Input: 123
        # Output: TypeError
        self.assertRaises(TypeError, to_upper, 123)
class TestToLower(unittest.TestCase):
    # Write you code here
    pass

class TestCapitalize(unittest.TestCase):
    # Write your code here
    pass

if __name__ == '__main__':
    unittest.main()
