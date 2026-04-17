n = int(input("Enter number: "))

def is_prime(num):
  flag = False
  if num == 0 or num == 1:
    print("Not prime number")
    return
  elif num > 1:
    for i in range(2, num):
      if(num % i) == 0:
        flag = True
        break
    if flag:
      print(num, "is not a prime number") 
      
    else:
      print(num, "is a prime number")   
      
is_prime(n)      
    
  