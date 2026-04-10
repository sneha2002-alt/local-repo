# Rectangle with constructor validation
class Rectangle:
  def __init__(self, width, height):
    self.width = width if width > 0 else 1.0
    self.height = height if height > 0 else 1.0
    
  def area(self):
    a = self.width * self.height 
    print("Area:", a)  
  
  
  def perimeter(self):
    p = 2 * (self.width + self.height )
    print("Perimeter:", p)    
    
r1 = Rectangle(3.4, 4.5) 
r1.area()
r1.perimeter()   
  
r2 = Rectangle(-3.4, -4.5) 
r2.area()
r2.perimeter()  

r3 = Rectangle(0,0) 
r3.area()
r3.perimeter()      
    