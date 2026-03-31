#if-elif-else SYNTAX

username = input("Enter username: ")
password = input("Enter password: ")

if(username == "admin" and password == "pass"):
  print("Login successful")
elif(username != "admin"):
  print("Wrong Username")
else:
  print("Wrong Password")  