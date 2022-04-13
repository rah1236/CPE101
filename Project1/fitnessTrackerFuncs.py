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
"""
1)Take User input of a String
2)Return the String that the user inputed
"""
    pass

# purpose:This function must user enters a negative or zero value and re-prompt for a valid value.
# signature: none -> Int
def input_age():
"""
1)Ask user for age input
2)assign user input to variable
3)confirm that input is valid integer
3)return input age
"""
    pass



# purpose:This function must prompt a user for a positive real value and return it.
#It must display an error message if the user enters a negative or zero value and re-prompt for a valid value.
# signature: none -> +Float
def input_height():
    """
    1)Ask user for height input
    2)assign user input to variable
    3)confirm that input is valid float
    3)return input float
    """
    pass

# purpose:This function must prompt a user for a positive real value and return it.
# It must display an error message if the user enters a negative or zero value and re-prompt for a valid value.
# signature:none -> +Float
def input_weight():
        """
        1)Ask user for weight input
        2)assign user input to variable
        3)confirm that input is valid float
        3)return input float
        """
    pass

# purpose:This function must prompt a user for a positive real value and return it.
# It must display an error message if the user enters a negative or zero value and re-prompt for a valid value.
# signature:none -> +Float
def input_duration():
        """
        1)Ask user for duration input
        2)assign user input to variable
        3)confirm that input is valid float
        3)return input float
        """
    pass

# purpose:his function must prompt a user for a positive integer value and return it.
# It must display an error message if the user enters a value < 1 or a value > 4, re-prompt for a valid value.
# signature:none -> +Int [1-4]
def input_exercise_type():
        """
        1)Ask user for exercise type input
        2)assign user input to variable
        3)confirm that input is valid int within range
        3)return input int
        """
    pass

# purpose:This function displays the information in the following order the floating point numbers must have 2 digits after decimal point.
# signature:String, Int, Float, Float, Float, Float, Float -> None
def print_info(name, age, height, weight, calorie_burned, BMI, miles):
    """
    1)Print info
    """
    pass

# purpose:This function takes weight in pounds and converts pounds to kilograms (weight(kg) = weight(lb) × 0.45359237).
# This function returns the weight in kilograms.
# signature: Float -> Float
def convert_lb_to_kg(weight):
        """
        1)convert weightto kg
        2)return converted weight in kg
        """
    pass

# purpose:This function takes the activity code and returns the METs’ number as an integer number.
# signature:Int -> Int
def compute_MET(exercise_type):
        """
        1)Take exercise type as input (int 1-4)
        2)look up equivalent MET met value and assign to var
        3)return variable with MET value
        """
    pass

# purpose: This function takes duration in minutes, weight in (kg), and MET value, and computes burned calories based on the given
# formula. The function returns that value.
# signature:Int, Float, Int -> Float
def compute_calorie_burned(duration, weight, met_value):
        """
        1)Take inputed duration weight and MET value
        2)Compute  Duration(in minutes)*(MET*3.5*weight in kg)/200
        3)return computed calories burned
        """
    pass

# purpose: his function takes weight in (lbs) and height in (inches), and computes BMI based on the given formula. The function returns the computed BMI value.
# signature: Float, Float -> Float
def compute_BMI(weight, height):
        """
        1)Take inputed weight and height
        2)Compute  703*weight(lb)/height(inch)^2
        3)return computed BMI
        """
    pass

# purpose: This function takes BMI and returns a message based on BMI value.
# signature: Float -> String
def BMI_category(BMI):
        """
        1)Take inputed BMI
        2)Check which of these intervals the BMI fits into:
        Underweight means BMI <18.59
        Normal Weight means BMI between 18.59–24.99 ( [18.59, 25) )
        Over Weight means BMI between 25–29.99 ( [25, 30) )
        Obesity means BMI of 30 or greater
        3)return type that BMI sits between
        """
    pass

# purpose:his function takes height in inches, exercise_type, and duration in minute and computes the miles using the given formula. This function returns the computed miles.
# signature: Float, Int, Int -> Float
def compute_equivalent_miles(height, exercise_type, duration):
        """
        1)Take inputed height, exercise type, and duration
        2)Compute  (0.413 * h ) /12  to find feet in one step and assign to var
        3)Check exercize type to find correct steps per minute and assign to variable
        4)Compute (stepsPerMinute * duration * feet per step * 1/5280)
        3)return computed Miles
        """
   pass
