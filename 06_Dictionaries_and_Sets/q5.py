# Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have key such as first_name, last_name, age and city. Print each piece of information stored in your dictionary

fav_person = {
    'first_name': 'Abhay',
    'last_name': 'Bhadouriya',
    'age': 21,
    'city': 'Gwalior'
}

for keys, values in fav_person.items():
    print(keys, ":" ,values)
    