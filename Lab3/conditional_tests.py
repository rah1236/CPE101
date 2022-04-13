# This is a header block example for lab 03.

# You will need to supply the following information.

# Name:Raheel Rehmatullah
# Section:7

import unittest
import conditional
from conditional import *

#You can delete pass after wrinting your code
class TestCases(unittest.TestCase):
   def test_max_of_2(self):
      self.assertEqual(conditional.max_of_2(1,2), 2)
      self.assertEqual(conditional.max_of_2(-4,7), 7)
      self.assertEqual(conditional.max_of_2(6,3), 6)
   def test_max_of_4(self):
      self.assertEqual(conditional.max_of_4(1,2,3,4), 4)
      self.assertEqual(conditional.max_of_4(-4,7, 2, 30), 30)
      self.assertEqual(conditional.max_of_4(6,3, 6, 19), 19)
   def test_letter_grade(self):
       self.assertEqual(conditional.letter_grade(100), "A")
       self.assertEqual(conditional.letter_grade(72), "C-")
       self.assertEqual(conditional.letter_grade(30), "F")
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
