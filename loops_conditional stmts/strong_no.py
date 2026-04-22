# Strong number => A number is said to be strong if the sum of factorial of digits in the number is equal to the number itself. 

n = int(input("Enter number: "))
original_n = n
sum = 0
while(n != 0):
      last = n % 10
      prod = 1
      for i in range(1, last+1):
              prod *= i
       
      sum += prod   
      n = n // 10
          
if sum == original_n:
        print(f"{original_n} is a strong number")                  
else:
        print("not a strong number")        