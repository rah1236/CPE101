#Name:Raheel Rehmatullah
#Section:7
#list comprehension tests

#takes list and spits out list of lists containing the og list seperated by 4 objects
#list - > list
def groups_of_4(numbers):
    newList = []
    newAdd = []
    if len(numbers) < 4 :
        return numbers
    else:
        critIndex = (len(numbers)) - (len(numbers)%4)
        for index in range(0,len(numbers), 4):
            if index != critIndex:
                for indexOf4 in range(index, index+4):
                    newAdd.append(numbers[indexOf4])
                newList.append(newAdd)
                newAdd = []
            else:
                for indexOfX in range(index, index + len(numbers)%4):
                    newAdd.append(numbers[indexOfX])
                newList.append(newAdd)
        return(newList)


#takes 2d array and a goal int and returns list of locations where that int can be found.
#list int -> list
def search_2D(objects, goal):
    newList = []
    for y in range(0, len(objects)):
        for x in range(0, len(objects[y])):
            if objects[y][x] == goal:
                newList.append((y,x))
    return newList
#takes list and sums summable values
#list -> int
def add_values(values):
    sum = 0
    for value in values:
        if type(value) is int:
            sum += value
        elif type(value) is list:
            for value2 in value:
                sum += value2
    return sum


#print(add_values([1, 2, [4, 5], 4, "a", [6, 5, 7], 9]))
#print(search_2D([[98, 90, 91], [46, 76, 62], [85, 90, 83], [77, 79, 81]] , 33))
