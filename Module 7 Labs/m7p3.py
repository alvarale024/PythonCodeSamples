#Alejando Alvarez
#6/15/2023
#P3,function multiplies all number in a list

def multiply_list_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

nums = [2, 3, 4, 5]
result = multiply_list_numbers(nums)
print(result)  



