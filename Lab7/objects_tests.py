#Name:
#Section:
import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_point(self):
       point = Point(5,4)
       self.assertEqual(point.x, 5)
       self.assertEqual(point.y, 4)
       self.assertEqual(repr(point), "x: 5 y: 4")
       self.assertEqual(point.__eq__(), False)
       self.assertEqual(point.distance(Point(5,4)), 0)

   def test_circle(self):
        circle = Circle(Point(1,2), 5)
        self.assertEqual(circle.center.x, 1)
        self.assertEqual(circle.center.y, 2)
        self.assertEqual(repr(circle), "#5 @(1 2)")
        self.assertEqual(circle.__eq__(circle), True)
        self.assertEqual(circle.overlaps(circle), True)









# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
