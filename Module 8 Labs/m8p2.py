#Alejandro Alvarez
#6/15/2023
#P2,Takes two user inputs and prints message if sum is less than, greater than, or equal to 10

def compare_sum_with_10():
    input1 = float(input("Enter the first number: "))
    input2 = float(input("Enter the second number: "))

    sum_result = input1 + input2

    if sum_result > 10:
        print("Sum is greater than 10.")
    elif sum_result < 10:
        print("Sum is less than 10.")
    else:
        print("Sum is equal to 10.")

compare_sum_with_10()
