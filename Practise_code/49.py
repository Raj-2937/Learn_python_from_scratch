#Write a program that catchs a ValueError when the user enters text instead of a number. 

try:
    # Ask for a number
    user_input = input("Enter a number: ")
    number = int(user_input)
    print("You entered the number:", number)

except ValueError:
    # Run this if they typed text instead of a number
    print("Error: That is text, not a number!")
