# Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person's name and their favorite number.

fav_nums = {
    'Abhay': 7,
    'Jeet': 3,
    'Aman': 4,
    'Dev': 9,
    'Abhishek': 13
}

for key, value in fav_nums.items():
    print(f"{key} favorite number is: {value}")
    
