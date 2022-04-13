# Name:Raheel Rehmatullah
# Section:7

#Returns the max of 2 given numbers
#Int Int -> Int
def max_of_2(num1, num2):
    if (num1 > num2):
        return num1
    elif (num1 < num2):
        return num2
    else:
        return num1
#Returns the max of 4 given numbers
#Int Int Int Int -> Int
def max_of_4(num1, num2, num3, num4):
    return(max_of_2(max_of_2(num1, num2), max_of_2(num3, num4)))


#Returns the corresponding letter grade depending on given integer grade
#Int -> String
def letter_grade(grade):
    if grade >= 93:
        return "A"
    elif grade >= 90:
        return "A-"
    elif grade >= 87:
        return "B+"
    elif grade >= 83:
        return "B"
    elif grade >= 80:
        return "B-"
    elif grade >= 77:
        return "C+"
    elif grade >= 73:
        return "C"
    elif grade >= 70:
        return "C-"
    elif grade >= 65:
        return "D"
    elif grade < 65:
        return "F"
