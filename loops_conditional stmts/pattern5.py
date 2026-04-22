n = int(input("Enter number: "))
for row in range(1,n+1):
        print(" " * (n-row),end="")
        print("*"*(2 * row - 1))
for row in range(n-1, 0, -1):
        print(" " * (n-row),end="")
        print("*"*(2 * row - 1))
        