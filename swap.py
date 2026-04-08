# Swapping without third variable
a  = int(input("Enter value of a: "))
b  = int(input("Enter value of b: "))

print("Before swapping value of a & b:", a,b)

a = a + b
b = a - b
a = a - b

print("After swapping value of a & b:", a,b)
