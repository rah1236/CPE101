# CPE 101-01
# LAB 6: Map Functions
# Name: Raheel Rehmatullah
# Section: 7

#purpose Cubes all elements in the list
# list -> list
def cube_all(numbers):
    return(list(map(lambda x: x**3, numbers)))

#adds arb number n to all elements in list
#list, Int - > list
def add_n_to_all(numbers, n):
    newList = []
    for number in numbers:
        newList.append(number+n)
    return(newList)

#divides every element in list by 5
#list->List
def div_by_5(numbers):
    newList = []
    count = 0
    while(count < len(numbers)):
        newList.append(numbers[count] / 5)
        count += 1
    return (newList)
