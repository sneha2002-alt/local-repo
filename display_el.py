# WAP that takes user input and stores them in a tuple, then displays the elements.
s = int(input("Enter size of tuple: "))

lst = []
for i in range(s):
    element = input(f"Enter element {i+1}: ")
    lst.append(element)

tup = tuple(lst)
print("Tuple:", tup)

print("Elements:", end=" ")
for val in tup:
    print(val, end=" ")
print()