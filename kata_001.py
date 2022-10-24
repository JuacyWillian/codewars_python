# You were camping with your friends far away from home, 
# but when it's time to go back, you realize that your fuel is 
# running out and the nearest pump is 50 miles away! 
# You know that on average, your car runs on about 25 miles per gallon. 
# There are 2 gallons left.

# Considering these factors, write a function that tells you if 
# it is possible to get to the pump or not.

# Function should return true if it is possible and false if not.


# Challenge
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if distance_to_pump<=(mpg*fuel_left) else False



# Tests
import unittest

class TestZeroFuelFunction(unittest.TestCase):

    def test_is_enough(self):
        self.assertEqual(zero_fuel(50, 25, 2), True)

    def test_is_not_enough(self):
        self.assertEqual(zero_fuel(100, 50, 1), False)

if __name__ == '__main__':
    unittest.main()
