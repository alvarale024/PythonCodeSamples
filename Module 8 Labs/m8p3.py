#Alejandro Alvarez
#6/15/2023
#P3,Function checks list for value of 5

def check_value_5(my_list):
    if 5 in my_list:
        print("Value 5 is in the list.")
    else:
        print("Value 5 is not in the list.")
        
nums = [1, 3, 5, 7, 9]
check_value_5(nums) 

nums = [2, 4, 6, 8, 10]
check_value_5(nums) 
