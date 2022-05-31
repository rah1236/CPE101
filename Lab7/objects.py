#Name:Raheel Rehmatullah
#Section:7
#list comprehension tests

import utility
import math

class Point:
    #inits point type
    #int int -> none
    def __init__(self, x:int , y:int):
        self.x = x
        self.y = y
    #checks if x and y are equal
    #none -> bool
    def __eq__ (self):
        return(utility.epsilon_equal(self.x,self.y))
    #prints string of object
    #none -> str
    def __repr__(self):
        return("x: " + str(self.x) + " y: " + str(self.y))
    #returns distance between 2 objects
    #point -> float
    def distance(self, otherPoint):
        return(math.sqrt((self.x - otherPoint.x)**2 + (self.y - otherPoint.y)**2))

class Circle:
        #inits circle type
        #none -> none
    def __init__(self, center:Point , radius:float):
        self.center = center
        self.radius = radius
    #returns if circle is equal to another circle
    #circle -> bool
    def __eq__ (self, otherCircle):
        return(self.radius == otherCircle.radius)
    #returns if self is smaller than another circle
    #circle -> bool
    def __lt__ (self, otherCircle):
        return(self.radius < otherCircle.radius)
    #prints string of object
    #none -> str
    def __repr__(self):
        return("#" + str(self.radius) + " @(" + str(self.center.x) + " " + str(self.center.y) + ")")
    #checks if one circle over laps another
    #circle -> bool
    def overlaps(self, otherCircle):
        return(self.center.distance(otherCircle.center) < self.radius + otherCircle.radius)
