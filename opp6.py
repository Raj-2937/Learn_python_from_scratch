# Inheritance types:
# - Single inheritance
# - Multi-level inheritance
# - Multiple inheritance



class A:
    varA = "Welcome to class A "
    
class B:
    varB = "Welcome to class B "
    
class C(A,B):
    varC = "Welcome to class C "

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)



# Class method: 
    
#     A class method is bound to the class and receives the class as an implicit first argument.
#     Note: static method cannot be accessed or modify class states, and generally for utility.

class student:
    @classmethod # decorator
    def collage (cls):
        pass
    
    
    
    
    
class Person:
    name = "anonymous" 
    def changename(self, name): 
        self.name = name
        
p1 = Person()
p1.changename("rahul kumar")
print(p1.name)
print(Person.name)