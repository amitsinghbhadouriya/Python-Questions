# Make a list of the multiples of 3, from 3 to 30. use a for loop to print the numbers in your list.

numbers = list(range(3,31))

for number in numbers:
    if number % 3 == 0:
        print(number)
