# Functions (have at least 4 functions)
# Project 2: Barista Coffee Assistant
#
# Name: Raheel Rehmatullah
# Section: 7
# Date:
#

#purpose: Input a string and make it all caps
#str -> str
def whole_str_capitalize(string):
    newString = ""
    for char in string:
        if ord(char) > 90:
            char = chr(ord(char) - 32)
        newString += char
    return(newString)

#purpose: Take a string and make the first char caps
#str->str
def str_capitalize(string):
    newString = ""
    for char in string:
        if len(newString) == 0:
            newString += whole_str_capitalize(char)
        else:
            newString += char
    return(newString)

#purpose: Ask user their coffee type
# none -> Str
def requestCoffeeType(userInput):
    userInput = userInput.lower()
    for x in range(0,3):
        if x > 0:
            userInput = input("What coffee type would you like? ").lower()
        #userInput = input("What coffee type would you like? ").lower()
        if (userInput == "americano" or userInput == "flat white" or userInput == "latte" or userInput == "espresso"):
            return userInput
        else:
            print("Sorry, that's not one of our options. Please Try again:")
    print("Sorry, we do not offer requested type.")
    exit()

#purpose Ask user if they want milk with their coffee
#none -> Bool
def requestCoffeeMilk(userInput):
    userInput = userInput.lower()
    for x in range(0,3):
        if x > 0 :
            userInput = input("Would you like milk in it? ").lower()
        #userInput = input("Would you like milk on the side? ").lower()
        if (userInput == "yes" or userInput == "y"):
            return True
        elif (userInput == "no" or userInput == "n"):
            return False
        else:
            print("Sorry, that's not one of our options.")
    print("Sorry, we can't help you.")
    exit()

#purpose Ask user for coffee size
#none -> string
def requestCoffeeSize(userInput):
    userInput = userInput.lower()
    for x in range(0,3):
        if x > 0 :
            userInput = input("What size will that be? ").lower()
        #userInput = input("Would you like your coffee Small, Medium, or Large? ").lower()
        if (userInput == "large" or userInput == "l"):
            return "l"
        elif (userInput == "medium" or userInput == "m"):
            return "m"
        elif (userInput == "small" or userInput == "s"):
            return "s"
        else:
            print("Sorry, that's not one of our options.")
    print("Sorry, we can't help you.")
    exit()


#purpose Ask user if they want their coffee to go.
#str -> Bool
def requestCoffeeToGo(userInput):
    userInput = userInput.lower()
    for x in range(0,3):
        if x > 0 :
            userInput = input("And will that be to go? ").lower()
        #userInput = input("Would you like your coffee to go? ").lower()
        if (userInput == "yes" or userInput == "y"):
            return True
        elif (userInput == "no" or userInput == "n"):
            return False
        else:
            print("Sorry, that's not one of our options.")
    print("Sorry, we can't help you.")
    exit()

#purpose: find price of coffee
#str str bool -> float
def findCoffeePrice(coffeeType, size, milkInIt):
    finalPrice = 0
    s = 0
    prices = {
    "flat white":[2.95, 3, 3.75],
    "americano":[2.75, 2.95, 3.25],
    "espresso":[2.75, 2.95, 3.25],
    "latte":[2.85, 3.75, 4.15]
    }
    if size == "s":
        s = 0
    elif size == "m":
        s = 1
    elif size == "l":
        s = 2
    if milkInIt:
        finalPrice += 0.25
    finalPrice += prices[coffeeType][s]
    return (finalPrice)
