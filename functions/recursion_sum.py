# WAF to calculate sum of first n natural numbers recursively.
def calc_sum(n):
  if(n == 0):
    return 0
  
  return calc_sum(n-1) + n
  
num = int(input("Enter number: "))
print("Sum:", calc_sum(num))  