# list
marks = [99, 97, 67, 87, 84, 99]
print(type(marks))
print(marks[2])
marks[2] = 88 # list is mutable
print(marks[2]) # indexing
print(marks[:3]) # slicing

# list methods
nums = [1, 2, 3, 5, 7, 4, 3, 5]

nums.append(10) # add element at the end
print(nums)

nums.insert(2,9) # insert element at given index
print(nums)

nums.reverse() # reverses our list
print(nums)

nums.sort() # sorts in ascending order
print(nums)

nums.sort(reverse=True) # sorts in descending order
print(nums)

nums.pop(2) # removes element at given index
print(nums)

nums.remove(3) # removes first occurrence of element
print(nums)