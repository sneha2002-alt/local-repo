# Exception Handling
try:
  x = int(input("Enter number: "))
  ans = (10/x)

except ZeroDivisionError:
  print("Division by zero is not allowed")

else:
  print("Answer:", ans)  
  
finally:
  print("End of program")  
    
  