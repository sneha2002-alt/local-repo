# WAP to print largest and smallest element in the list.
lst = [1, 2, 3, 4, 5, 6]

largest = lst[0]
smallest = lst[0]
i = 1

while i < len(lst):
  if(lst[i] > largest):
    largest = lst[i] 
  if(lst[i] < smallest):
    smallest = lst[i]  
  i += 1
  
print(f"Largest = {largest}, Smallest = {smallest}")
   
    
    
    
