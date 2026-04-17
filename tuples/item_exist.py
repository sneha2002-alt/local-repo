# Check if a given element exists in a tuple.
tup = (1,2,3,4,56,6)

x = 56
idx = 0
found = False
for val in tup:
  if(x == val):
    print("Element found at index:", idx)
    found = True
    break
  idx += 1

if not found:
    print("Element not found in tuple") 