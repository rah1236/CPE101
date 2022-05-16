# CPE 101-01
# LAB 6: Map Function Tests
# Name: Raheel Rehmatullah
# Section: 7

import unittest
import nested

class TestPoly(unittest.TestCase):
   #do not delete this part, use this to comapre two lists
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_cube_all(self):	# Tests for add function
      self.assertListAlmostEqual(nested.product([[0,0,0], [1,2,3,4]]), [0, 24])
      self.assertListAlmostEqual(nested.product([[1,1,1], [2,5,8]]), [1, 80])
      self.assertListAlmostEqual(nested.product([[1,4,0], [2,3], [30, 1, 3]]), [0, 6, 90])


if __name__ == '__main__':
   unittest.main()
