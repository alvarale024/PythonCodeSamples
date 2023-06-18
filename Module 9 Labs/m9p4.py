#ALejandro Alvarez
#6/16/2023
#P4,Program runs through numbers ranging from 0-50 and prints all numbers divisible by 10 in a list

counter = 0
tens = []

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("List of numbers divisible by 10:")
print(tens)

