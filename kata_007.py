"""
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.

"""


# Solution
def boolean_to_string(b):
    return 'True' if b else 'False'


# Tests
import unittest

class TestBooleanToString(unittest.TestCase):
    def test_boolean_to_string(self, ):
        self.assertEqual(boolean_to_string(True), "True")
        self.assertEqual(boolean_to_string(False), "False")

if __name__=='__main__':
    unittest.main()