# Make a function that will return a greeting statement that uses an input; 
# your program should return, "Hello, <name> how are you doing today?".

# [Make sure you type the exact thing I wrote or the program may not execute properly]


# Challenge
def greet(name):
    return f"Hello, {name} how are you doing today?"



# Tests
import unittest

class TestZeroFuelFunction(unittest.TestCase):

    def test_greetings(self, ):
        self.assertEqual(greet('Ryan'), "Hello, Ryan how are you doing today?", "Passed")
        self.assertEqual(greet('Shingles'), "Hello, Shingles how are you doing today?", "Passed")


if __name__ == '__main__':
    unittest.main()
