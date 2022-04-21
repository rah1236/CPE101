# Main Program
# Project 1 Fitness Tracking
#
# Name: Raheel Rehmatullah
# Section: 7
# Date:
import fitnessTrackerFuncs
def main():
    fitnessTrackerFuncs.welcome()
    while True:
        name = fitnessTrackerFuncs.input_name()
        age = fitnessTrackerFuncs.input_age()
        height = fitnessTrackerFuncs.input_height()
        weight = fitnessTrackerFuncs.input_weight()
        exercise_type = fitnessTrackerFuncs.input_exercise_type()
        METs = fitnessTrackerFuncs.compute_MET(exercise_type)
        BMI = fitnessTrackerFuncs.compute_BMI(weight, height)
        bodyType = fitnessTrackerFuncs.BMI_category(BMI)
        duration = fitnessTrackerFuncs.input_duration()
        miles = fitnessTrackerFuncs.compute_equivalent_miles(height, METs, duration)
        caloriesBurned = fitnessTrackerFuncs.compute_calorie_burned(duration, weight, fitnessTrackerFuncs.compute_MET(exercise_type))
        fitnessTrackerFuncs.print_info(name, age, height, weight, caloriesBurned, bodyType, miles)
        restartProgram = False
        restartProgram = (str(input("Would you like to apply fitness tracking to another user (y/n): ")))
        restartProgram = (restartProgram == "y" or restartProgram == "Y")

        if(not restartProgram):
            break



if __name__ == '__main__':
    main()
