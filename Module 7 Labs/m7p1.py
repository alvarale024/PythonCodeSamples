#Alejando Alvarez
#6/15/2023
#P1,Prints radius of a circle

import math

def areaOfCircle(r):
    area = math.pi * math.pow(r, 2)
    return area

radius = float(input("Enter the radius of the circle: "))
circle_area = areaOfCircle(radius)
print("The area of the circle with radius", radius, "is:", circle_area)
