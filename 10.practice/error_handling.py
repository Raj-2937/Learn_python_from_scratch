age = int(input("Enter your age: "))
print(age)


try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Please enter a valid number.")