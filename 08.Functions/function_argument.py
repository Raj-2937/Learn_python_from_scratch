def average(a = 9,b =1):
     print("The average is " , (a+b)/2)
    
average(1,5)


def average(a , b , c =1):
    print('The average is ' , (a+b+c)/2)
    


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is " , sum / len(numbers))
    
average(5,6)
