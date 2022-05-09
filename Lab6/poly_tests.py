# CPE 101-01
# LAB 6: Polynomial Function Tests
# Name: Raheel Rehmatullah
# Section: 7

import unittest
from poly import *

class TestPoly(unittest.TestCase):
   #do not delete this part, use this to comapre two lists
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_polyadd(self):	# Tests for add function
      pass



if __name__ == '__main__':
   unittest.main()
