# Odd numbers from 1 to n
n = int(input("Enter N: "))
i = 0
while (i < n):
  i+=1
  if(i % 2 == 0):
    continue
  print(i)