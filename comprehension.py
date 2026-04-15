words = ['apple', 'hi', 'banana', 'a', 'python']

words = [val for val in words if len(val)>3]
print(words)

lst = ['apple', 'hi', 'banana', 'a', 'python']
lst = [len(i) for i in lst]
print(lst)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]


flat = [val for row in matrix for val in row]
print("Flattened:", flat)

result = [val for val in flat if val > 4]
print("Values > 4:", result)

grades = [75, 88, 42, 95, 60]

grades = ["Pass" if scores>=50  else "Fail" for scores in grades]

print(grades)

grade = [75, 88, 42, 95, 60]

grade = [score for score in grade if score>= 70]
print(grade)