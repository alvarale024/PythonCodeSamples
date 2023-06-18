#Alejando Alvarez
#6/15/2023
#P4,Function takes list of number and creates unique list with elements of first list

def get_unique_elements(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

my_list = [1, 3, 3, 3, 6, 2, 3, 5]
result = get_unique_elements(my_list)
print(result)



