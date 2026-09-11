#  oops, in Python. 
#  To map with real-world scenarios, we have started using objects in code. 
#  This is called object-oriented programming 

#Class and object in Python

# Class is a blueprint for creating objects.

class Student: 
    
    name="Karan Kumar"
    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in database..")

# creating object (instance)
s1 = Student("karan" )
print(s1.name) #karan
s2 = Student("Arjun")
print(s2.name)
s3 =Student("Aryan")
print(s3.name)




# class car:
#     color = "green"
#     brand = "mercedes"
    
# car1 = car()
# print(car1.color)
# print(car1.brand)

#methods
#methods are function that belong tp objects. 

#1Q

class students:  
    def __init__(self, name , marks):
        self.name = name 
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val  
        print("hi", self.name , "young avg score is:",sum/3)
        
s1 = students("tony starks ", [99,98,97])
s1.get_avg()


#static methods
# Methods that do not use the `self` parameter (work at the class level) 

class student:
    @staticmethod
    def collage():
        print("ABC Collage")
        
#Important:
    
#Abstraction, hiding the implementation details of a class and only showing the initial features to the user.         
        
#Encapsulation:
#wrapping data and functions into a single unit object         
        
        
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")
        
car1 = car()
car1.start()


#3Q
class acount:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc 
    
    #debit method 
    def debit(self,amount):
        self.balance =- amount 
        print("Rs." ,amount , "was debited")
        print("total balance = " ,self.get.balance())
    
    
    def credit(self,amount):
        self.balance += amount 
        print("Rs." ,amount , "was credited")
        print("total balance = " ,self.get.balance())

    def get_balance(self):
        return  seff.balance
     
acc1 =  Account(10000 , 12345)     
print(acc1.balcnce)
print(acc1.account_no)

