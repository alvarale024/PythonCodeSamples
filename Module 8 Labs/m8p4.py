#Alejandro Alvarez
#6/15/2023
#P4,Function checks if a year fits the parameters of a gap year 

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
year = 2020
result = is_leap_year(year)
print(result)

year = 2021
result = is_leap_year(year)
print(result)
