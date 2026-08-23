# Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow' or 'red'. 
# If the alien color is green, print a message that the player just earned 5 points for shooting the alien.
# if the alien color is yellow, print a message that the player just earned 10 points.
# if the alien color is red, print a message that the player just earned 15 points.
alien_color = input("Enter a color, (must be 'green', 'yellow', 'red'): ")

if alien_color == 'green':
    print("You earned 5 points")
elif alien_color == 'yellow':
    print("You earned 10 points")
else:
    print("You earned 15 points")