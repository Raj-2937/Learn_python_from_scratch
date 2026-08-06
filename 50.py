#write a calculater that catches both Valueerror and zerodivion. 

try:
    #get user input
    num1 = int(input("enter 1st number:"))
    operator = input("choose a for calculation (+,-,*,/):")
    num2 = int(input("enter you 2nd number:"))
    
# perform calculation.
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    
    else:
        print("envalid operator!")
    
except ValueError:
    print("enter only number for calculation , not type text!")
    
except ZeroDivisionError:
    print("please! don't enter o for calculation ok, you can not divide a number by number!")