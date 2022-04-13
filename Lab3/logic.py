# Name:Raheel Rehmatullah
# Section:7

# Returns whether or not it is true that int is test_is_even
# Int -> Boolean
def is_even(number):
    return(number % 2 == 0)


# Returns whether or not a number is within the provided intervals
# Int -> Boolean
def in_an_interval(number):
    intervalCase1 = (number >= -12) and (number < -6)
    intervalCase2 = (number >= -2) and (number <= 5)
    intervalCase3 = (number > 15) and (number < 28)
    intervalCase4 = (number > 42) and (number <= 52)
    intervalCase5 = (number >= 110) and (number <= 237)

    return(intervalCase1 or intervalCase2 or intervalCase3 or intervalCase4 or intervalCase5)

# takes two number arguments and returns True when the 1st argument
#is in the (60, 140] interval and is divisible to 2nd
#argument, which is in the interval of [-10,40]
# Int Int -> Boolean
def is_divisible_in_interval(num1, num2):
    inInterval1 = (num1 > 60) and (num1 <= 140)
    isDivisible = num1 % num2 == 0
    inInterval2 = (num2 >= -10) and (num2 <= 40)

    return (inInterval1 and inInterval2 and isDivisible)
