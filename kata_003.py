# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

#    solution('abc', 'bc') # returns true
#    solution('abc', 'd') # returns false


def solution(string, ending):
    return string.endswith(ending)




# Tests
import unittest

class TestSameEnds(unittest.TestCase):
    def test_endswith_same_char(self, ):
        self.assertEqual(solution("abcde", "cde"), True, "")
        self.assertEqual(solution("abcde", "abc"), False, "")
        self.assertEqual(solution('ails', ''), True, "")
        self.assertEqual(solution('this', 'fails'), False, "")
        self.assertEqual(solution('sumo', 'omo'), False, "")

if __name__ == '__main__':
    unittest.main()
