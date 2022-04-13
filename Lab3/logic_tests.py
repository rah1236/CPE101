
# This is a header block example for lab 03.

# You will need to supply the following information.

# Name:Raheel Rehmatullah
# Section:7

import unittest
import logic
from logic import *

#You can dlete pass after wrinting your code
class TestCases(unittest.TestCase):
   def test_is_even (self):
       self.assertEqual(logic.is_even(5), False)
       self.assertEqual(logic.is_even(2), True)
       self.assertEqual(logic.is_even(-4), True)
   def test_in_an_interval (self):
       self.assertEqual(logic.in_an_interval(-8), True)
       self.assertEqual(logic.in_an_interval(-3), False)
       self.assertEqual(logic.in_an_interval(4), True)
       self.assertEqual(logic.in_an_interval(32), False)
       self.assertEqual(logic.in_an_interval(52), True)
       self.assertEqual(logic.in_an_interval(147), True)
   def test_is_divisible_in_interval (self):
        self.assertEqual(logic.is_divisible_in_interval(70,7), True)
        self.assertEqual(logic.is_divisible_in_interval(100,20), True)
        self.assertEqual(logic.is_divisible_in_interval(85,35), False)
        self.assertEqual(logic.is_divisible_in_interval(40,20), False)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
