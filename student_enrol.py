# Student Enrollments
list = [
  ("Alice", "Math"),
  ("Bob", "Science"),
  ("Alice", "Science"),
  ("Charlie", "Math"),
  ("Bob", "Math"),
  ("Alice", "English"),
  ("Charlie", "English")
]

# list of all unique courses
unique_courses_set = set()

for tup in list:
  unique_courses_set.add(tup[1]) # course
print(unique_courses_set) 

# list students enrolled in English
for name, course in list:
   if(course == "English"):
     print(name)

# dictionary(student, set of courses)  
dict = {}

for name, course in list:
  if(dict.get(name) == None):
    dict.update({name : set()})
    dict[name].add(course)
  else:
    dict[name].add(course)

print(dict)
   

     