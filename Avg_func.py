#function to calculate average of 3 numbers
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
n3=int(input("Enter 3rd number:"))

def calc_avg(a,b,c):
  avg= (a + b + c)/3
  return avg

print(calc_avg(n1,n2,n3))  