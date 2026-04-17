# Create a dictionary of students and their marks, then print the name of the student with the highest marks. 
students = {
   "Alice": 85,
    "Bob": 72,
    "Charlie": 93,
    "Diana": 88
}

highest_marks = 0

for name, marks in students.items():
  print(name, ":", marks)
  if (marks> highest_marks):
    highest_marks = marks
    top_student = name

print("Student with highest marks:", top_student)
