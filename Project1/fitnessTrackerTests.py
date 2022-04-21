# Project 1 Fitness Tracking Tests
# At least 2 tests for each function
# Name: Raheel Rehmatullah
# Section: 7
# Date:

import unittest
import fitnessTrackerFuncs
class MyTestCase(unittest.TestCase):
    def test_convert_lb_to_kg(self):
        self.assertAlmostEqual(fitnessTrackerFuncs.convert_lb_to_kg(5), 2.26796185)
        self.assertAlmostEqual(fitnessTrackerFuncs.convert_lb_to_kg(200), 90.718474)
    def test_compute_calorie_burned(self):
        self.assertAlmostEqual(fitnessTrackerFuncs.compute_calorie_burned(5,5,5), 2.1875 )
        self.assertAlmostEqual(fitnessTrackerFuncs.compute_calorie_burned(20, 30, 1), 10.5 )
    def test_compute_BMI(self):
        self.assertAlmostEqual(fitnessTrackerFuncs.compute_BMI(4320, 43), 1642.4878312601406 )
        self.assertAlmostEqual(fitnessTrackerFuncs.compute_BMI(200, 70), 28.693877551020407 )
    def test_compute_equivalent_miles(self):
        self.assertAlmostEqual(fitnessTrackerFuncs.compute_equivalent_miles(5,5,5), 0.01955492424242424 )
        self.assertAlmostEqual(fitnessTrackerFuncs.compute_equivalent_miles(20, 3, 2130), 27.767992424242426  )

if __name__ == '__main__':
    unittest.main()
