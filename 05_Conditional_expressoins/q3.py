# A spam comments is defined as a text containing following keywords.
# "make a lot of money", "buy now", "subscribe this", "click this". 
# Write a program to detect these spams

text = input("Enter a message: ")
if "make a lot of money" == text or "buy now" == text or "subscribe this" == text or "click this" == text:
    print("This is a spam keyword")
else: 
    print("This is not a spam keyword")