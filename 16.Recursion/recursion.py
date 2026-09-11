# recursion 
# when a function calls itslef repeatedly. 

#print n to 1 backwards 

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5)

# Factorial function 

def fact(n):
    if (n == 1 or n ==0):
        return 1
    else:
        return n * fact(n-1)
print(fact(6))
