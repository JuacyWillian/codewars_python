"""
Complete the function that accepts a string parameter, 
and reverses each word in the string. All spaces in the 
string should be retained.

Examples:
    "This is an example!" ==> "sihT si na !elpmaxe"
    "double  spaces"      ==> "elbuod  secaps"
"""


# Solution
def solution(s): 
    words = s.split(' ')
    reversed_words = str.join(' ', [w[::-1] for w in words])
    return reversed_words


# Tests
import unittest

class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self, ):
        self.assertEqual(solution(""), "")
        self.assertEqual(solution('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
        self.assertEqual(solution('apple'), 'elppa')
        self.assertEqual(solution('a b c d'), 'a b c d')
        self.assertEqual(solution('double  spaced  words'), 'elbuod  decaps  sdrow')

if __name__=='__main__':
    unittest.main()