
# This is a header block example for lab 03.

# You will need to supply the following information.

# Name: Raheel Rehmatullah
# Section: 7

import unittest
import power4Table


#You can dlete pass after wrinting your code
class TestCases(unittest.TestCase):
   def test_factorial (self):
      self.assertEqual(power4Table.factorial(5), 120)
      self.assertEqual(power4Table.factorial(-8), 40320)
      self.assertEqual(power4Table.factorial(2.6534), 2)


   def test_income_tax (self):
      self.assertEqual(power4Table.income_tax(5), 0.1)
      self.assertEqual(power4Table.income_tax(10000), 0.12)
      self.assertEqual(power4Table.income_tax(42000), 0.22)
      self.assertEqual(power4Table.income_tax(90000), 0.24)
      self.assertEqual(power4Table.income_tax(200000), 0.32)

   def test_total_avg(self):
        self.assertEqual(power4Table.total_avg(1, 500), 252.0)
        self.assertEqual(power4Table.total_avg(-848, 40000), 19575.5)
        self.assertEqual(power4Table.total_avg(111, 333), 220.5)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
