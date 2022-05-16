# CPE 101-01
# LAB 6: Filter Function Tests
# Name: Raheel Rehmatullah
# Section: 7

import unittest
import filter

class TestPoly(unittest.TestCase):
   #do not delete this part, use this to comapre two lists
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_are_even(self):	# Tests for add function
      self.assertListAlmostEqual(filter.are_even([0,0,0]), [0, 0, 0])
      self.assertListAlmostEqual(filter.are_even([1,1,1]), [])
      self.assertListAlmostEqual(filter.are_even([1,4,0]), [4, 0])

   def test_remove_duplicates(self):	# Tests for add function
      self.assertListAlmostEqual(filter.remove_duplicates([0,0,0]), [0,])
      self.assertListAlmostEqual(filter.remove_duplicates([1,1,1]), [1])
      self.assertListAlmostEqual(filter.remove_duplicates([1,4,0]), [1, 4, 0])

   def test_are_even(self):	# Tests for add function
      self.assertListAlmostEqual(filter.are_divisible_by_n([0,0,0] , 1), [0, 0, 0])
      self.assertListAlmostEqual(filter.are_divisible_by_n([10, 20, 45], 5), [10, 20, 45])
      self.assertListAlmostEqual(filter.are_divisible_by_n([1,4,0], 1), [1, 4, 0])

if __name__ == '__main__':
   unittest.main()
