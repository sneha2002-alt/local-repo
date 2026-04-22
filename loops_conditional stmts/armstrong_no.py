# Armstrong Number
n = int(input("Enter number: "))
a,temp = n,n
count = 0
sum = 0
while(n != 0):
      n = n // 10
      count += 1
        
while(temp != 0):
      last = temp % 10
      sum += last ** count 
      temp = temp // 10 
if sum == a:
      print("Armstrong number")
else:
      print("Not armstrong number")                   