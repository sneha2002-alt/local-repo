class Laptop:
  storage_type = "ssd"
  
  def __init__(self, RAM, storage):
    self.RAM = RAM
    self.storage = storage
    
  @classmethod  # Class method
  def get_storage_type(cls):
    print(f"storage type = {cls.storage_type}")  
    
  def get_info(self):   # Instance method
    print(f"Laptop has {self.RAM} RAM and {self.storage} storage")  
    
  @staticmethod  # Static Method
  def calc_discount(price, discount):
    final_price = price - (discount*price/100)
    print(f"discounted price = {final_price}")
    
l1 = Laptop("16GB", "512GB")    
l2 = Laptop("8GB", "256GB")    

l1.get_info()
l1.get_storage_type()
l1.calc_discount(40_000, 10)
Laptop.get_storage_type()