# Function Tests Program
# Project 2: Barista Coffee Assistant
#
# Name: Raheel Rehmatullah
# Section:7
# Date:
#
import baristaCoffeeFuncs
import unittest
class MyTestCase(unittest.TestCase):
    def test_requestCoffeeType(self):
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeType("AmEricano"), "americano")
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeType("FLAT WHITE"), "flat white")
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeType("latte"), "latte")

    def test_requestCoffeeMilk(self):
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeMilk("y"), True)
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeMilk("yES"), True)
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeMilk("n"), False)

    def test_requestCoffeeSize(self):
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeSize("mediUm"), "m")
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeSize("LARGE"), "l")
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeSize("small"), "s")

    def test_requestCoffeeToGo(self):
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeToGo("yes"), True)
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeToGo("No"), False)
        self.assertEqual(baristaCoffeeFuncs.requestCoffeeToGo("n"), False)

    def test_findCoffeePrice(self):
        self.assertEqual(baristaCoffeeFuncs.findCoffeePrice("americano", "l", False), 3.25)
        self.assertEqual(baristaCoffeeFuncs.findCoffeePrice("latte", "s", False), 2.85)
        self.assertEqual(baristaCoffeeFuncs.findCoffeePrice("flat white", "l", True), 4)

if __name__ == '__main__':
    unittest.main()
