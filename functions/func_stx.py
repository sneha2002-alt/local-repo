
cities = ["delhi", "mumbai", "agra", "pune"]
fruits = ["apple", "litchi", "banana", "orange", "kiwi"]

# WAF to print length of the list.
def print_len(list):
  print(len(list))
  
print_len(cities)  
print_len(fruits)  

# WAF to print elements of a list in a single line.
def print_items(list):
  for i in list:
    print(i, end = " ")
    
print_items(fruits)    

# WAF to convert USD to INR.
amount = int(input("\nEnter amount in USD: "))

def convert(usd_val):
  inr_val = usd_val * 93
  print(usd_val, "USD = ", inr_val, "INR")
  
convert(amount)  