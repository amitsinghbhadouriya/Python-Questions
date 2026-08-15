# Write a program to sum a list with 4 numbers.

list = [3,5,6,7]

sum = list[0] + list[1] + list[2] + list[3]
print("Sum through normal addition:", sum)

new_sum = 0
for item in list:
    new_sum = new_sum + item
    
print("Sum through for loop:", new_sum)