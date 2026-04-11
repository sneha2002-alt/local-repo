class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self, other): # dunder function greater than 
       return self.price > other.price    
        
o1 = Order("chips", 20)        
o2 = Order("tea", 15)      

print(o1 > o2) 
        