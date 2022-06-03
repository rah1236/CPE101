# Main Program
# Project 2: Barista Coffee Assistant
#
# Name: Raheel Rehmatullah
# Section: 7
# Date:
#
from baristaCoffeeFuncs import *
def main():
    while(True):
        coffeeType = requestCoffeeType(input("What coffee type would you like? "))
        if coffeeType == "americano" or coffeeType == "espresso":
            milkInIt = requestCoffeeMilk(input("Would you like milk in it? "))
        else:
            milkInIt = False
        size = requestCoffeeSize(input("What size will that be? "))
        togo = requestCoffeeToGo(input("And will that be to go? "))
        price = findCoffeePrice(coffeeType, size, milkInIt)

        print(str_capitalize(coffeeType))
        if (milkInIt):
            print("Milk on the side")
        else:
            print("No extras")
        if togo:
            print("Takeout")
        else:
            print("In cafe")
        print("Please pay ${:.2f} to the cashier".format(price))

        print()
        print()

        again = input("Would you like anything else? ").lower()
        if  again == "n" or again == "no":
            exit()


if __name__ == '__main__':
    main()
