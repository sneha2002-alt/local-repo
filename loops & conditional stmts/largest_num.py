#WAP to check largest of 4 numbers
num1 = int(input("Enter 1st num:"))
num2 = int(input("Enter 2nd num:"))
num3 = int(input("Enter 3rd num:"))
num4 = int(input("Enter 4th num:"))
largest = num1
if( num2 > largest):
    largest = num2
if(num3 > largest):
  largest = num3
if(num4 > largest):
  largest = num4
print("Largest is:",largest)

