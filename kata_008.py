"""
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, 
he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number 
of litres Nathan will drink, rounded to the smallest value.

For example:
    time = 3 ----> litres = 1
    time = 6.7---> litres = 3
    time = 11.8--> litres = 5
"""


# Solution
def litres(time):
    return time // 2


# Tests
import unittest

class TestLitres(unittest.TestCase):
    def test_litres(self, ):
        self.assertEqual(litres(2), 1, 'should return 1 litre')
        self.assertEqual(litres(1.4), 0, 'should return 0 litres')
        self.assertEqual(litres(12.3), 6, 'should return 6 litres')
        self.assertEqual(litres(0.82), 0, 'should return 0 litres')
        self.assertEqual(litres(11.8), 5, 'should return 5 litres')
        self.assertEqual(litres(1787), 893, 'should return 893 litres')
        self.assertEqual(litres(0), 0, 'should return 0 litres')

if __name__=='__main__':
    unittest.main()