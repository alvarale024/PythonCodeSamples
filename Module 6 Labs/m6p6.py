#Alejandro Alvarez
#6/12/2023
#P6,Prints facatorials of a number using the "for" loop and math module

import math

number = int(input("Enter a number: "))

factorial = 1
for i in range(1, number + 1):
    factorial *= i

print("Factorial (using a for loop):", factorial)

factorial_math = math.factorial(number)
print("Factorial (using math module):", factorial_math)
