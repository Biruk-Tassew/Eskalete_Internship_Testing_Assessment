import unittest
from string_functions import *

class TestToUpper(unittest.TestCase):

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
    # Test the to_lower functions.

    def test_to_lower(self):
        # Assert with all capital letters string
        # Input: "HELLO"
        # Output: "hello"
        self.assertEqual(to_lower("HELLO"), "hello")

        # Assert with a mixed lower and upper letters.
        # Input: "HeLlO"
        # Output: "hello"
        self.assertEqual(to_lower("HeLlO"), "hello")
        
        # Assert with a numerical digits.
        # Input: "HeLlO"
        # Output: "hello"
        self.assertEqual(to_lower("12B3"), "12b3")

        # Assert empty string.
        # Input: "HeLlO"
        # Output: "hello"
        self.assertEqual(to_lower(""), "")

class TestCapitalize(unittest.TestCase):
    # Test the capitalize functions.

    def test_capitalize(self):

        # Assert with all small letters string
        # Input: "hello"
        # Output: "Hello"
        self.assertEqual(capitalize("hello"), "Hello")

        # Assert a string with a mix of small and capital letters.
        # Input: "HeLlO"
        # Output: "Hello"
        self.assertEqual(capitalize("HeLlO"), "Hello")
        
        # Assert with a numerical digits.
        # Input: "HeLlO"
        # Output: "hello"
        self.assertEqual(capitalize("12B3"), "12b3")

        # Assert empty string.
        # Input: "HeLlO"
        # Output: "hello"
        self.assertEqual(capitalize(""), "")
        
if __name__ == '__main__':
    unittest.main()
