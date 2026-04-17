#if-elif-else SYNTAX

username = input("Enter username: ")
password = input("Enter password: ")

if(username == "admin" and password == "pass"):
  print("Login successful")
elif(username != "admin"):
  print("wrong username, try again.")
else:
  print("wrong password, try again.")  