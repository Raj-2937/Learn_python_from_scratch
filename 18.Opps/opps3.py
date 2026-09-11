# Private attributes and methods:
#     conceptual implementations in Python.
#     Private attributes and methods are meant to be used only within the class and are not accessible from outside the class. 

class account:
    def __init__(self,acc_no , acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass
    
      
acc1 = account("12345" ,"abcd")

print(acc1.acc_no)
print(acc1.__acc_pass)