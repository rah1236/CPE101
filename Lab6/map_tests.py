# CPE 101-01
# LAB 6: Map Function Tests
# Name: Raheel Rehmatullah
# Section: 7

import unittest
import map

class TestPoly(unittest.TestCase):
   #do not delete this part, use this to comapre two lists
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_cube_all(self):	# Tests for add function
      self.assertListAlmostEqual(map.cube_all([0,0,0]), [0, 0, 0])
      self.assertListAlmostEqual(map.cube_all([1,1,1]), [1, 1, 1])
      self.assertListAlmostEqual(map.cube_all([1,4,0]), [1, 64, 0])

   def test_add_n_to_all(self):	# Tests for add function
        self.assertListAlmostEqual(map.add_n_to_all([0,0,0], 7), [7, 7, 7])
        self.assertListAlmostEqual(map.add_n_to_all([1,1,1], 49), [50, 50, 50])
        self.assertListAlmostEqual(map.add_n_to_all([1,4,0], -3), [-2, 1, -3])

   def test_div_by_5(self):	# Tests for add function
        self.assertListAlmostEqual(map.div_by_5([0,0,0]), [0, 0, 0])
        self.assertListAlmostEqual(map.div_by_5([1,1,1]), [0.20, 0.20, 0.20])
        self.assertListAlmostEqual(map.div_by_5([1,4,0]), [0.20, 0.80, 0])


if __name__ == '__main__':
   unittest.main()
