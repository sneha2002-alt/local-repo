# List comprehensions

squares = [i*i  for i in range(6) if i % 2 != 0]
print(squares)

nums = [-2, -6, 5, 3, 8, -1]

nums = [0 if val < 0 else val for val in nums]
print(nums)

words = ["hello", "python", "books"]

words = [val.upper() for val in words]
print(words)