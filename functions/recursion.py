# Factorial using Recursion
def fact(n):
  if( n == 0 or n == 1):
    return 1
  else:
    return n * fact(n-1)
  
num = int(input("Enter number: "))  
print(f"Factorial of {num}:",fact(num))  