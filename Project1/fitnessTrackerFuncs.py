# Project 1 Fitness Tracking
#
# Name: Raheel Rehmatullah
# Section: 7
# Date:

# purpose: splay the welcome message.
# signature: None -> none
def welcome():
    print("""
    Welcome to Fitness Tracker Application!

    To begin you must specify the participant's name, age, heigt (in inches),
    weight (in lbs), exercise duration (in minutes), and exercise type (1-4)!
    Now you can compute the burned calories and BMI.
    """)

# purpose: This function must prompt a user for the name.
# signature: None -> String
def input_name():
    return(str(input("Enter the name: ")))


# purpose:This function must user enters a negative or zero value and re-prompt for a valid value.
# signature: none -> Int
def input_age():
    age = int(input("Enter the age: "))
    if age<0:
        print("Age can't be less than zero, try again")
        age = input("Enter the age: ")
    else:
        return(int(age))

# purpose:This function must prompt a user for a positive real value and return it.
#It must display an error message if the user enters a negative or zero value and re-prompt for a valid value.
# signature: none -> +Float
def input_height():
        height = float(input("Enter the height in inches: "))
        if height<0:
            print("Height can't be less than zero, try again")
            height = input("Enter the height in inches: ")
        else:
            return(float(height))


# purpose:This function must prompt a user for a positive real value and return it.
# It must display an error message if the user enters a negative or zero value and re-prompt for a valid value.
# signature:none -> +Float
def input_weight():
        weight = float(input("Enter the weight in pounds: "))
        if weight<0:
            print("Weight can't be less than zero, try again")
            weight = input("Enter the weight in pounds: ")
        else:
            return(float(weight))

# purpose:This function must prompt a user for a positive real value and return it.
# It must display an error message if the user enters a negative or zero value and re-prompt for a valid value.
# signature:none -> +Float
def input_duration():
        duration = float(input("Enter the duration in minutes: "))
        if duration<0:
            print("Duration can't be less than zero, try again.")
            height = input("Enter the duration in minutes: ")
        else:
            return(float(duration))

# purpose:his function must prompt a user for a positive integer value and return it.
# It must display an error message if the user enters a value < 1 or a value > 4, re-prompt for a valid value.
# signature:none -> +Int [1-4]
def input_exercise_type():
        type = int(input("Enter the excersize type: 1)low-impact 2)high-impact 3)slow-paced 4)fast-paced "))
        if type<1 or type>4:
            print("That isn't a number from 1-4, try again.")
            type = input("Enter the excersize type: 1)low-impact 2)high-impact 3)slow-paced 4)fast-paced ")
        else:
            return(int(type))


# purpose:This function displays the information in the following order the floating point numbers must have 2 digits after decimal point.
# signature:String, Int, Float, Float, Float, Float, Float -> None
def print_info(name, age, height, weight, calorie_burned, BMI_category, miles):
    print("{:^6}".format("Name: " + str(name)))
    print("{:^6}".format("Age: " + str(age)))
    print("{:^6}".format("Height: " + str(height)))
    print("{:^6}".format("Weight: " + str(weight)))
    print("Miles: {:.2f}".format(miles))
    print("{:^6}".format("Burned Calories: "+ str(calorie_burned)))
    print("{:^6}".format("BMI Category: " + str(BMI_category)))


#print_info("name", "age", "height", "weight","calorie_burned", "pee", 8)

# purpose:This function takes weight in pounds and converts pounds to kilograms (weight(kg) = weight(lb) × 0.45359237).
# This function returns the weight in kilograms.
# signature: Float -> Float
def convert_lb_to_kg(weight):
    return(float(weight*0.45359237))


# purpose:This function takes the activity code and returns the METs’ number as an integer number.
# signature:Int -> Int
def compute_MET(exercise_type):
    if exercise_type == 1:
        return 5
    elif exercise_type == 2:
        return 7
    elif exercise_type == 3:
        return 3
    elif exercise_type == 4:
        return 4



# purpose: This function takes duration in minutes, weight in (kg), and MET value, and computes burned calories based on the given
# formula. The function returns that value.
# signature:Int, Float, Int -> Float
def compute_calorie_burned(duration, weight, met_value):
    return(duration * (met_value * 3.5 * weight)/200)

# purpose: his function takes weight in (lbs) and height in (inches), and computes BMI based on the given formula. The function returns the computed BMI value.
# signature: Float, Float -> Float
def compute_BMI(weight, height):
    return((703*weight)/(height*height))


# purpose: This function takes BMI and returns a message based on BMI value.
# signature: Float -> String
def BMI_category(BMI):
    if BMI<18.59:
        return "Underweight"
    elif (BMI <= 24.99 and BMI >= 18.59):
        return "Normal Weight"
    elif (BMI <= 30 and BMI >= 25):
        return "Over Weight"
    elif (BMI > 30):
        return "Obesity"


# purpose:his function takes height in inches, exercise_type, and duration in minute and computes the miles using the given formula. This function returns the computed miles.
# signature: Float, Int, Int -> Float
def compute_equivalent_miles(height, METs, duration):
    feetPerStep = (0.413 * height/12)
    stepsPerMinute = 0
    if METs == 5:
        stepsPerMinute = 120
    elif METs == 7:
        stepsPerMinute = 227
    elif METs == 3:
        stepsPerMinute = 100
    elif METs == 4:
        stepsPerMinute = 152

    return(stepsPerMinute * duration * feetPerStep * (1.0/5280.0))
