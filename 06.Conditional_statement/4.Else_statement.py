"""else statement"""
#else runs when all above conditions are False.
#It does not have a condition.

#example

marks =int(input("enter your marks:"))

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
