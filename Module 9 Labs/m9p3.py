#ALejandro Alvarez
#6/16/2023
#P3,Program asks users to enter numbers until the sum of the numbers entered is greater than 100

numbers = []
total_sum = 0

while total_sum <= 100:
    num = int(input("Enter a number: "))
    numbers.append(num)
    total_sum += num

print("Sum of the numbers is greater than 100.")
print("Numbers entered:", numbers)
