n = int(input("Enter num: "))
for i in range(n+1,1,-1):
        print(" "*((n+1)-i),end="")
        for j in range(1,i):
               print(j,end="")
           
        print()