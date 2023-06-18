#Alejando Alvarez
#6/15/2023
#P2,python function that check wether a number is between 1-10 

def is_between_1_and_10(number):
    if number >= 1 and number <= 10:
        return True
    else:
        return False

num = 11
result = is_between_1_and_10(num)
print(result)  



