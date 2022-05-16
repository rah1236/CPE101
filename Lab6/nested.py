# CPE 101-01
# LAB 6: Nested Functions
# Name: Raheel Rehmatullah
# Section: 7

# returns a list of integers such that each integer is product of its inner list.
#list -> list
def product(numberList):
    newList = []
    for list in numberList:
        product = 0
        for index in range(0, len(list)):
            if index == 0:
                product = list[index]
            else:
                product *= list[index]
        newList.append(product)
    return(newList)
