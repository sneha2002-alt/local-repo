# Create a list of numbers and remove duplicates
lst = []
s = int(input("Enter size of list: "))

for i in range(s):
  num = int(input(f"Enter element {i+1}: "))
  lst.append(num)
  
print("Original list:",lst)

unique = []
for num in lst:
  if num not in unique:
    unique.append(num)
    
print("After removing duplicates:",unique)    
