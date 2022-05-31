#Name:Raheel Rehmatullah
#Section: 7
#unittest for objects

import math
from objects import *


def distance(point, otherPoint):
    return(math.sqrt((point.x - otherPoint.x)**2 + (point.y - otherPoint.y)**2))

#computes and returns a list containing the distance from the origin (0, 0) to the corresponding point in the input list.
#list - > list_comp
def distance_all(circles):
    return([i for i in circles ]

circles = [Circle(Point(1,2), 5)]

distance_all(circles)
