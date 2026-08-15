# Write a program to detect double space in a string and replace it with single space

Message = "Hey  How  are  you  what  you  learn  about  python"
detect_double_space = Message.find("  ")
print(Message)
print(detect_double_space)

Single_space = Message.replace("  ", " ")
print(Single_space)