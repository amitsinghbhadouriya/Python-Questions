# Write a python function to remove a given word from a string and strip it at the same time.

def rem_word(string, word):
    new_str = string.replace(word, "")
    return new_str.strip()

message = "     Python is best    "
n = rem_word(message, "Python")
print(n)