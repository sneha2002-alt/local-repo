# Using loops with lists
nums = [1,2,3,4,5]

x = 5
idx = 0

for val in nums:
  if(val == x):
    print(f"{x} is found at index = {idx}")
    break
  idx+=1

# printing all list values using loops  
for val in nums:
  print(val)  
  