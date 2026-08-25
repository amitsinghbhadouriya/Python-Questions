# Write a program to create a dictionary of hindi words with value as their english translation. Provide user with an option to loop it up!

Words = {
    'kitab': "Book",
    'billi': "Cat",
    'Kutta': "Dog",
    'Pahad': "Mountain"
}

word = input("Enter a word: ")

print(Words.get(word, "Word not found"))