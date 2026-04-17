# Bank Account basics 
class BankAccount:
  def __init__(self, acc_holder, balance = 0.0):
    self.acc_holder = acc_holder
    self.balance = balance
    self.acc_number = "ACC"+ f"{int(balance):04d}"
    
  def deposit(self, amount):
    self.balance += amount 
    
  def get_balance(self):
    print(f"Account number {self.acc_number} has current balance: {self.balance}") 
    
b1 = BankAccount("Aman") 
b1.deposit(1000)    
b1.get_balance()