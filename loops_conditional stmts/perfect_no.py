# Perfect Number => n is called as a perfect no. if the sum of all factors of n excluding itself is equal to n.
n = int(input("Enter number: "))
sum = 0
for i in range(1, n):
    
        if n%i == 0:
                sum += i
if sum == n:
        print(f"{n} is a perfect number")
else:
        print("not a perfect number")        