# CPE 101-01
# LAB 6: Polynomial Function Tests
# Name: Raheel Rehmatullah
# Section: 7

import unittest
import poly

class TestPoly(unittest.TestCase):
   #do not delete this part, use this to comapre two lists
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_polyadd(self):	# Tests for add function
      self.assertListAlmostEqual(poly.poly_add2([0,0,0], [1, 1, 1]), [1, 1, 1])
      self.assertListAlmostEqual(poly.poly_add2([1,1,1], [1, 1, 1]), [2, 2, 2])
      self.assertListAlmostEqual(poly.poly_add2([1,4,0], [21.3, 1.0949343, 1]), [22.3, 5.0949343, 1])

   def test_polymultiply(self):	# Tests for add function
      self.assertListAlmostEqual(poly.poly_multiply2([0,0,0], [1, 1, 1]), [0, 0, 0, 0, 0])
      self.assertListAlmostEqual(poly.poly_multiply2([1,1,1], [1, 1, 1]), [1, 2, 3, 2, 1])
      self.assertListAlmostEqual(poly.poly_multiply2([2,2,2], [1, 1, 1]), [2, 4, 6, 4, 2])



if __name__ == '__main__':
   unittest.main()
