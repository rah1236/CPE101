#Name:Raheel Rehmatullah
#Section: 7
#unittest for objects
import unittest
from nested_list import *

class TestCases(unittest.TestCase):
   def test_groups_of_4(self):
      self.assertEqual(groups_of_4([1,2,3,4,5,6,7]), [[1, 2, 3, 4], [5, 6, 7]])
      self.assertEqual(groups_of_4([1,2,3,4,5,6,7,8,9,10]), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]])
      self.assertEqual(groups_of_4([1,2,3, 4]), [[1, 2, 3, 4]])

   def test_search_2D(self):
       self.assertEqual(search_2D([[1,2,3,4,5,6,7]], 1), [(0,0)])
       self.assertEqual(search_2D([[1,2],[2,1]], 1), [(0, 0), (1, 1)])
       self.assertEqual(search_2D([[0]], 1), [])

   def test_add_values(self):
       self.assertEqual(add_values([[1,2,3,4,5,6,7]]), 28)
       self.assertEqual(add_values([[1,2],[2,1]]),6)
       self.assertEqual(add_values([[0]]), 0)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
