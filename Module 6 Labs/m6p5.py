#Alejandro Alvarez
#6/12/2023
#P5,Takes two user inputs (side A & B) to calculate a side c using the puthagorean theorem

import math

a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print("The length of side c is:", c)
