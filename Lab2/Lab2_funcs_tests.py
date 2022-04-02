#Lab 2 Test Cases
#Name:Raheel Rehmatullah
#Section:CPE-101-07-2224
##############################################################
import unittest
import funcs
import math
#3 test cases for each function
class TestCases(unittest.TestCase):
   def test_do_math(self):
       self.assertAlmostEqual(funcs.do_math(1,1), 0.07246376811594202)
       self.assertAlmostEqual(funcs.do_math(0,0), 0)
       self.assertAlmostEqual(funcs.do_math(10,10), -3.1223628691983114)
       pass

   def test_quadratic_formula1(self):
      self.assertAlmostEqual(funcs.quadratic_formula1(1, 2, 1), -1.0)
      self.assertAlmostEqual(funcs.quadratic_formula1(1, 1, 0), 0)
      self.assertAlmostEqual(funcs.quadratic_formula1(1, 0, 0), 0)
      pass

   def test_quadratic_formula2(self):
      self.assertAlmostEqual(funcs.quadratic_formula2(1, 2, 1), -1.0)
      self.assertAlmostEqual(funcs.quadratic_formula2(1, 1, 0), -1.0)
      self.assertAlmostEqual(funcs.quadratic_formula2(1, 0, 0), 0)
      pass

   def test_distance(self):
      self.assertAlmostEqual(funcs.distance(1, 1, 1, 1), 0)
      self.assertAlmostEqual(funcs.distance(1, 0, 1, 0), 0)
      self.assertAlmostEqual(funcs.distance(0, 0, 1, 1), math.sqrt(2))
      pass

   def test_is_negative(self):
      self.assertAlmostEqual(funcs.is_negative(5), False)
      self.assertAlmostEqual(funcs.is_negative(0), False)
      self.assertAlmostEqual(funcs.is_negative(-3), True)
      pass

   def test_dividable_by_5(self):
    self.assertAlmostEqual(funcs.dividabe_by_5(5), True)
    self.assertAlmostEqual(funcs.dividabe_by_5(1), False)
    self.assertAlmostEqual(funcs.dividabe_by_5(-3), False)
    pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
