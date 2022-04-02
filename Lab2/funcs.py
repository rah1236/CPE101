#Lab 2 Functions
#Name: Raheel Rehmatullah
#Section:CPE-101-07-2224
import math

#1)purpose statement:This function compute a given formula
# signature:int int -> float
def do_math (x, y):
    return (x*x - (4.0/3.0)*x*y*y)/(((2*y*x*x)/5.0)-5.0)
    pass

#2)purpose statement: This function gives the positive outcome of the Quadratic equation
# signature: int int int -> float
def quadratic_formula1 (a, b, c):
    return (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    pass

#3)purpose statement:This function gives the negative outcome of the Quadratic equation
# signature:int int int -> float
def quadratic_formula2 (a, b, c):
    return (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    pass

#4)purpose statement:This function calculates the distance between 2 2d points
# signature: int int int int -> float
def distance (x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    pass

#5)purpose statement:This function detirmines if a number is negative
# signature: int -> bool
def is_negative (num):
    return(num < 0)
    pass

#6)purpose statement:This function detirmines if a number is divisible by 5
# signature:int -> bool
def dividabe_by_5 (num):
    return ((num%5) == 0)
    pass
