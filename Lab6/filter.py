# CPE 101-01
# LAB 6: Filter Functions
# Name: Raheel Rehmatullah
# Section: 7

#returns a list of all even values in the input list.
#list - > list
def are_even(numbers):
    newList = []
    count = 0
    while(count < len(numbers)):
        if number % 2 == 0:
            newList.append(number)
            count += 1
    return(newList)

#returns a list with duplicate numbers removed
#list->list
def remove_duplicates(numbers):
    newList = []
    for number in numbers:
        if (number not in newList):
            newList.append(number)
    return(newList)

#checks if all elements in a list are divisible by n and returns them
#list, int -> list
def are_divisible_by_n(numbers, n):
    newList = [number for number in numbers if (number%n == 0)]
    return(newList)
