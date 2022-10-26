# Complete the solution so that it reverses the string passed into it.
#
#   Example:
#         'world'  =>  'dlrow'
#         'word'   =>  'drow'


# Solution
def solution(string):
    return str.join('', [s for s in string[::-1]])


# Tests
import unittest

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self, ):
        self.assertEqual(solution('world'), 'dlrow')
        self.assertEqual(solution('hello'), 'olleh')
        self.assertEqual(solution(''), '')
        self.assertEqual(solution('h'), 'h')


if __name__ == '__main__':
    unittest.main()
