class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(f"{self.real}i + {self.img}j")
        
    def __add__(self, num2): #dunder function
        new_real = self.real + num2.real  
        new_img = self.img + num2.img  
        return Complex(new_real, new_img)
          
    def __sub__(self, num2): #dunder function
        new_real = self.real - num2.real  
        new_img = self.img - num2.img  
        return Complex(new_real, new_img)
    
    
    
             
        
num1 = Complex(8, 4)
num1.showNumber() 
num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()
       