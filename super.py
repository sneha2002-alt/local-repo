class Car:
    def __init__(self, type):
        self.type = type  
     
    @staticmethod    
    def start():
        print("car started...")    
        
    @staticmethod    
    def stop():
        print("car stopped...")        
        
class ToyotaCar(Car):
    def __init__(self, name, type):
        super().start() 
        super().__init__(type)   # super keyword
        self.name = name  
        

c1 = ToyotaCar("prius", "electric")
print(c1.name, c1.type)        