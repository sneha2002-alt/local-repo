#logical operators in expression

age = int(input("Enter age:"))

if(age < 13):
  print("child")
elif(age >= 13 and age < 18):
  print("teenager")
else:
  print("adult")  