# Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal number end in th, except 1,2, and 3.
# Store the numbers 1 through 9 in a list.
# Loop through the list.
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read 1st, 2nd and so on , and each result should be on a separate line.

ordinal_numbers = [1,2,3,4,5,6,7,8,9]

for number in ordinal_numbers:
    if number == 1:
        print(f"The number is: {number}st")
    elif number == 2:
        print(f"The number is: {number}nd")
    elif number == 3:
        print(f"The number is: {number}rd")
    else:
        print(f"The number is: {number}th")