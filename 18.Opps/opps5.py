# Inheritance:
# when a class (child/derieved) derives the properties and methods of another class (parent / base).

class car:
    color = "black"
    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod 
    def stop():
        print("car stopped.")
class toyotacar(car):
    def __init__(self,brand):
        self.brand = brand 
        super().__init__(type)
        super().start
        
        
        
class fortuner(car):
    def __intit__(self,type):
        self.type = type
        
car3 = fortuner("disel")
car3.start()   

     
car1 = toyotacar("fortunar")
car2 = toyotacar("prius")
    
print(car1.name)
print(car1.start())




# Inheritance types:
# - Single inheritance
# - Multi-level inheritance
# - Multiple inheritance




