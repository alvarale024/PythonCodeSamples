#Alejandro Alvarez
#6/7/2023
#prints numbers ranging from 1-50 and prints if a number is divisible by 3, 5, or both

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both")
    elif num % 3 == 0:
        print("Divisible by 3")
    elif num % 5 == 0:
        print("Divisible by 5")
    else:
        print(num)
