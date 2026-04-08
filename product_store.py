class Products:
  count = 0
  def __init__(self, name, price):
    self.name = name
    self.price = price
    Products.count += 1
    
  def get_info(self):
    print(f"price of {self.name} is Rs.{self.price}") 
  
  @classmethod  
  def get_count(cls):  
    print(f"total products in store = {cls.count}") 
    
  @staticmethod
  def calc_discount(price, discount):
    final_price = price - (discount * price / 100)
    print(f"discounted price = {final_price}")
    
    
p1 = Products("Pen", 10)
p2 = Products("Pencil", 5)
p3 = Products("Notebook", 50)
p4 = Products("Phone", 10_000)
p5 = Products("Charger", 200)
p6 = Products("Keychain", 20)


p1.get_info()    

Products.get_count()
p1.calc_discount(p1.price, 12)