# Project 1 Fitness Tracking
#
# Name: Raheel Rehmatullah
# Section: 7
# Date:

# purpose: splay the welcome message.
# signature: None -> none
def welcome():
    Print("""
    Welcome to Fitness Tracker Application!

    To begin you must specify the participant's name, age, heigt (in inches),
    weight (in lbs), exercise duration (in minutes), and exercise type (1-4)!
    Now you can compute the burned calories and BMI.
    """)

# purpose: This function must prompt a user for the name.
# signature: None -> String
def input_name():
    return(str(Input("Enter the name: ")))
# purpose:This function must user enters a negative or zero value and re-prompt for a valid value.
# signature: none -> Int
def input_age():
    while True:
        userInput = int(input("Enter the age: ")
        if (userInput <= 0):
            print("Error! " + str(userInput) + " wasn't a valid age.")
        else:
            return(userInput)
            break



# purpose:This function must prompt a user for a positive real value and return it.
#It must display an error message if the user enters a negative or zero value and re-prompt for a valid value.
# signature: none -> +Float
def input_height():
    pass

# purpose:This function must prompt a user for a positive real value and return it.
# It must display an error message if the user enters a negative or zero value and re-prompt for a valid value.
# signature:none -> +Float
def input_weight():
    pass

# purpose:This function must prompt a user for a positive real value and return it.
# It must display an error message if the user enters a negative or zero value and re-prompt for a valid value.
# signature:none -> +Float
def input_duration():
    pass

# purpose:his function must prompt a user for a positive integer value and return it.
# It must display an error message if the user enters a value < 1 or a value > 4, re-prompt for a valid value.
# signature:none -> +Int [1-4]
def input_exercise_type():
    pass

# purpose:This function displays the information in the following order the floating point numbers must have 2 digits after decimal point.
# signature:String, Int, Float, Float, Float, Float, Float -> None
def print_info(name, age, height, weight, calorie_burned, BMI, miles):
    pass

# purpose:This function takes weight in pounds and converts pounds to kilograms (weight(kg) = weight(lb) × 0.45359237).
# This function returns the weight in kilograms.
# signature: Float -> Float
def convert_lb_to_kg(weight):
    pass

# purpose:This function takes the activity code and returns the METs’ number as an integer number.
# signature:Int -> Int
def compute_MET(exercise_type):
    pass

# purpose: This function takes duration in minutes, weight in (kg), and MET value, and computes burned calories based on the given
# formula. The function returns that value.
# signature:Int, Float, Int -> Float
def compute_calorie_burned(duration, weight, met_value):
    pass

# purpose: his function takes weight in (lbs) and height in (inches), and computes BMI based on the given formula. The function returns the computed BMI value.
# signature: Float, Float -> Float
def compute_BMI(weight, height):
    pass

# purpose: This function takes BMI and returns a message based on BMI value.
# signature: Float -> String
def BMI_category(BMI):
    pass

# purpose:his function takes height in inches, exercise_type, and duration in minute and computes the miles using the given formula. This function returns the computed miles.
# signature: Float, Int, Int -> Float
def compute_equivalent_miles(height, exercise_type, duration):
   pass
